"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import FileResponse, Http404
from django.conf import settings
from django.views.generic import TemplateView

import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# Optional: serve legacy .html files under project root
def serve_html_legacy(request, filename):
    base = settings.BASE_DIR.parent  # project root with your HTML files
    file_path = os.path.join(base, filename)
    if not os.path.exists(file_path):
        raise Http404('Page not found')
    return FileResponse(open(file_path, 'rb'))

# Serve other assets (css/js/images) directly from project root (dev convenience)
ALLOWED_EXTS = {'.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
                '.webp', '.ttf', '.woff', '.woff2', '.mp3', '.mp4', '.json', '.txt'}

def serve_asset(request, path):
    base = settings.BASE_DIR.parent
    _, ext = os.path.splitext(path)
    if ext.lower() not in ALLOWED_EXTS:
        raise Http404('Asset type not allowed')
    file_path = os.path.join(base, path)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        raise Http404('Asset not found')
    return FileResponse(open(file_path, 'rb'))

urlpatterns += [
    re_path(r'^(?P<filename>.*\\.html)$', serve_html_legacy),
    re_path(r'^(?P<path>(?!api/).+\\.(css|js|png|jpg|jpeg|gif|svg|ico|webp|ttf|woff|woff2|mp3|mp4|json|txt))$', serve_asset),
]
