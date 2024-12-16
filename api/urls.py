from django.urls import path
from api import views  # 引入 views

urlpatterns = [
    path('line_webhook/', views.line_webhook, name='line_webhook'),
]
