"""hipBackend URL Configuration

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
from django.urls import path,include
from hipBackend import views

from django.conf import settings  #官方要求的引用方式
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hipud/', include('hip_useradmin.urls')), # 分布式路由，挂载上hip_useradmin的路由
    path('',views.indexpage), # 后台小首页
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
