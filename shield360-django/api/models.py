from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('child', 'Child'),
        ('guardian', 'Guardian'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='child')
    age = models.PositiveIntegerField(null=True, blank=True)
    guardian = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children_rel')
    preferences_language = models.CharField(max_length=8, default='en')
    preferences_font_size = models.CharField(max_length=16, default='medium')
    preferences_high_contrast = models.BooleanField(default=False)

class Module(models.Model):
    CATEGORY_CHOICES = (
        ('personal-safety', 'Personal Safety'),
        ('digital-safety', 'Digital Safety'),
        ('mental-health', 'Mental Health'),
        ('legal-rights', 'Legal Rights'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    description = models.TextField()
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    animation_url = models.URLField(blank=True, null=True)
    badge_name = models.CharField(max_length=100, blank=True, null=True)
    badge_icon = models.CharField(max_length=32, blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    quiz_results = models.JSONField(default=list)
    badges_earned = models.JSONField(default=list)

class Report(models.Model):
    CASE_STATUS = (
        ('pending', 'pending'),
        ('reviewed', 'reviewed'),
        ('in-progress', 'in-progress'),
        ('resolved', 'resolved'),
    )
    case_id = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=32)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.JSONField(default=dict)
    status = models.CharField(max_length=16, choices=CASE_STATUS, default='pending')
    priority = models.CharField(max_length=16, default='medium')
    anonymous = models.BooleanField(default=True)
    attachments = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Alert(models.Model):
    ALERT_TYPES = (
        ('sos', 'sos'),
        ('emotional-distress', 'emotional-distress'),
        ('quiz-low-score', 'quiz-low-score'),
        ('module-completion', 'module-completion'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts_user')
    guardian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts_guardian')
    type = models.CharField(max_length=32, choices=ALERT_TYPES)
    message = models.TextField()
    location = models.JSONField(default=dict)
    emotion = models.CharField(max_length=16, blank=True, null=True)
    severity = models.CharField(max_length=16, default='medium')
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatbotMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    emotion = models.CharField(max_length=16, blank=True, null=True)
    sentiment_score = models.FloatField(default=0)
    flagged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
