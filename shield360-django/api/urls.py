from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('auth/register', views.register),
    path('auth/login', views.login_view),
    # Users
    path('users/profile', views.profile),
    path('users/preferences', views.update_preferences),
    path('users/children', views.children),
    # Modules
    path('modules', views.modules_list),
    path('modules/<str:module_id>', views.module_detail),
    path('modules/progress/<str:user_id>', views.user_progress),
    path('modules/<str:module_id>/progress', views.submit_progress),
    # Reports
    path('reports', views.create_report),
    path('reports/my-reports', views.my_reports),
    # Chatbot
    path('chatbot/chat', views.chatbot_chat),
    path('chatbot/history', views.chatbot_history),
    # SOS
    path('sos/send', views.sos_send),
    path('sos/alerts', views.sos_alerts),
    # Admin
    path('admin/analytics', views.admin_analytics),
]


