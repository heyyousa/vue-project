from django.urls import path
from hip_useradmin import views

urlpatterns = [
    path('get_uicons/',views.get_uicons), # 前端获取用户头像的api
    path('update_icons/', views.update_icons), # 后台更新头像库api

]

