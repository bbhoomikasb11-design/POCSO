from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Module, Progress, Report, Alert, ChatbotMessage
from .serializers import (
    UserSerializer, RegisterSerializer, ModuleSerializer,
    ProgressSerializer, ReportSerializer, AlertSerializer, ChatbotMessageSerializer
)
import random
import string

def issue_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = issue_token_for_user(user)
        return Response({
            'token': token,
            'user': UserSerializer(user).data
        }, status=201)
    return Response({'message': serializer.errors}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'message': 'Invalid credentials'}, status=401)
    if not user.check_password(password):
        return Response({'message': 'Invalid credentials'}, status=401)
    token = issue_token_for_user(user)
    return Response({
        'token': token,
        'user': UserSerializer(user).data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response(UserSerializer(request.user).data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_preferences(request):
    user = request.user
    prefs = request.data or {}
    user.preferences_language = prefs.get('language', user.preferences_language)
    user.preferences_font_size = prefs.get('fontSize', user.preferences_font_size)
    user.preferences_high_contrast = prefs.get('highContrast', user.preferences_high_contrast)
    user.save()
    return Response(UserSerializer(user).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def children(request):
    if request.user.role != 'guardian':
        return Response({'message': 'Access denied'}, status=403)
    kids = request.user.children_rel.all()
    return Response(UserSerializer(kids, many=True).data)

@api_view(['GET'])
@permission_classes([AllowAny])
def modules_list(request):
    mods = Module.objects.all().order_by('order')
    return Response(ModuleSerializer(mods, many=True).data)

@api_view(['GET'])
@permission_classes([AllowAny])
def module_detail(request, module_id):
    try:
        m = Module.objects.get(id=module_id)
        return Response(ModuleSerializer(m).data)
    except Module.DoesNotExist:
        return Response({'message': 'Module not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_progress(request, user_id):
    entries = Progress.objects.filter(user_id=user_id).select_related('module')
    data = []
    for p in entries:
        item = ProgressSerializer(p).data
        # embed module details similar to populate
        item['moduleId'] = ModuleSerializer(p.module).data
        data.append(item)
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_progress(request, module_id):
    quiz_results = request.data.get('quizResults', [])
    score = int(request.data.get('score', 0))
    try:
        m = Module.objects.get(id=module_id)
    except Module.DoesNotExist:
        return Response({'message': 'Module not found'}, status=404)
    badges = []
    if score >= 70 and m.badge_name:
        badges = [{'name': m.badge_name, 'icon': m.badge_icon}]
    p, _ = Progress.objects.update_or_create(
        user=request.user, module=m,
        defaults={
            'quiz_results': quiz_results,
            'score': score,
            'completed': True,
            'completed_at': timezone.now(),
            'badges_earned': badges,
        }
    )
    return Response(ProgressSerializer(p).data)

def generate_case_id():
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f'SHIELD-{int(timezone.now().timestamp()*1000)}-{suffix}'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_report(request):
    data = request.data.copy()
    data['case_id'] = generate_case_id()
    data['user'] = request.user.id
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        report = serializer.save()
        return Response(ReportSerializer(report).data, status=201)
    return Response({'message': serializer.errors}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_reports(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return Response(ReportSerializer(reports, many=True).data)

def analyze_sentiment(text):
    t = (text or '').lower()
    positive = any(w in t for w in ['happy','good','great','fine','okay','well','better','excited'])
    negative_hits = sum(w in t for w in ['sad','bad','angry','scared','worried','stressed','anxious','hurt','help'])
    if negative_hits > 2:
        return {'emotion':'stressed','score':-0.7,'flagged':True}
    if negative_hits > 0 and not positive:
        return {'emotion':'sad','score':-0.4,'flagged':False}
    if positive:
        return {'emotion':'happy','score':0.6,'flagged':False}
    return {'emotion':'neutral','score':0,'flagged':False}

def get_response(emotion):
    messages = {
        'happy': [
            "That's wonderful to hear! I'm glad you're feeling good. Is there anything specific you'd like to talk about?",
            "I'm so happy that you're feeling positive! Remember, it's great to share your feelings.",
        ],
        'sad': [
            "I'm sorry you're feeling down. It's okay to feel sad sometimes. Would you like to talk about what's bothering you?",
            "I understand that you're feeling sad. You're not alone, and I'm here to listen. What would make you feel better?",
        ],
        'stressed': [
            "It sounds like you might be going through a difficult time. Would you like me to connect you with a counselor?",
            "I can sense you're feeling stressed. Your feelings are valid. Want to share more or talk to a real counselor?",
        ],
        'neutral': [
            "I'm here to listen. How can I help you today?",
            "Thank you for sharing. Is there anything specific you'd like to discuss?",
        ],
    }
    return random.choice(messages.get(emotion, messages['neutral']))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chatbot_chat(request):
    message = request.data.get('message', '')
    sentiment = analyze_sentiment(message)
    response_text = get_response(sentiment['emotion'])
    msg = ChatbotMessage.objects.create(
        user=request.user,
        message=message,
        response=response_text,
        emotion=sentiment['emotion'],
        sentiment_score=sentiment['score'],
        flagged=sentiment['flagged'],
    )
    # Create alert to guardian if flagged
    if sentiment['flagged'] and request.user.guardian_id:
        Alert.objects.create(
            user=request.user,
            guardian_id=request.user.guardian_id,
            type='emotional-distress',
            message='Emotional distress detected in SafeSpace conversation',
            emotion=sentiment['emotion'],
            severity='high'
        )
    return Response({'response': response_text, 'emotion': sentiment['emotion'], 'flagged': sentiment['flagged']})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chatbot_history(request):
    items = ChatbotMessage.objects.filter(user=request.user).order_by('-created_at')[:50]
    return Response(ChatbotMessageSerializer(items, many=True).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sos_send(request):
    location = request.data.get('location', {})
    message = request.data.get('message', 'SOS Alert - Immediate assistance needed')
    user = request.user
    if not user.guardian_id:
        return Response({'message': 'No guardian assigned'}, status=400)
    alert = Alert.objects.create(
        user=user,
        guardian_id=user.guardian_id,
        type='sos',
        message=message,
        location=location,
        severity='critical'
    )
    return Response({'success': True, 'message': 'SOS alert sent to guardian', 'alert': AlertSerializer(alert).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sos_alerts(request):
    if request.user.role != 'guardian':
        return Response({'message': 'Access denied'}, status=403)
    alerts = Alert.objects.filter(guardian=request.user).select_related('user').order_by('-created_at')
    data = AlertSerializer(alerts, many=True).data
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_analytics(request):
    if request.user.role != 'admin':
        return Response({'message': 'Access denied'}, status=403)
    overview = {
        'totalUsers': User.objects.count(),
        'totalReports': Report.objects.count(),
        'totalAlerts': Alert.objects.count(),
        'totalProgress': Progress.objects.filter(completed=True).count(),
    }
    reports_by_status = list(Report.objects.values('_id=models.F(\"status\")').annotate(count=Count('id')).values('status','count'))
    alerts_by_type = list(Alert.objects.values('_id=models.F(\"type\")').annotate(count=Count('id')).values('type','count'))
    module_completions = list(Progress.objects.filter(completed=True).values('module').annotate(count=Count('id')))
    return Response({
        'overview': overview,
        'reportsByStatus': reports_by_status,
        'alertsByType': alerts_by_type,
        'moduleCompletions': module_completions,
    })
from django.shortcuts import render

# Create your views here.
