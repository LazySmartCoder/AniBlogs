"""AniBlogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler500, handler404
from django.views.static import serve

urlpatterns = [
    path('AniBlogs/anirbanbhattacharyaAniBlogzAdmin/', admin.site.urls),
    path('', include("AniBlogsWebsite.urls")),
    re_path(r'^Images/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT}),
]
admin.site.site_header = "AniBlogs Admin Panel"
admin.site.index_title = "Welcome to AniBlogs"
admin.site.site_title  = "AniBlogs"
handler404 = "AniBlogsWebsite.views.handle404"
handler500 = "AniBlogsWebsite.views.handle500"