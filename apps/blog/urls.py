from django.urls import path
from apps.blog import views

urlpatterns = [
    path('blog', views.BlogView.as_view()),  # 获取博客信息
]
