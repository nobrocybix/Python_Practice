from django.urls import path
from . import views

app_name = 'learning_logs'  # 設置應用程式名稱

urlpatterns = [
    # 主頁
    path('', views.index, name='index'),
]