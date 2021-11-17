from django.urls import path
from apps.blog import views

urlpatterns = [
    path('', views.BlogView.as_view()),  # 获取博客信息
]
