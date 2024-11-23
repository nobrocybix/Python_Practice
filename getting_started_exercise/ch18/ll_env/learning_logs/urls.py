from django.urls import re_path
from . import views

app_name = 'learning_logs'  # 設置應用程式名稱

urlpatterns = [
    # 主頁
    re_path(r'^$', views.index, name='index'),

    # 顯示所有的主題
    re_path(r'^topics/$', views.topics, name='topics'),

    # 特定主題的詳細頁面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]