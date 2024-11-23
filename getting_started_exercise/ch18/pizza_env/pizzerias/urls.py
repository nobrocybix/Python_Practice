from django.urls import re_path
from . import views

app_name = 'pizzerias'  # 設置應用程式名稱

urlpatterns = [
    # 主頁
    re_path(r'^$', views.index, name='index'),
    
    # 顯示供應的披薩
    re_path(r'^pizzas/$', views.pizzas, name='pizzas'),

    # 特定披薩的詳細頁面
    re_path(r'pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]