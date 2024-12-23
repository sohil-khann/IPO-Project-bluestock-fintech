from django.urls import path
from . import views

urlpatterns = [
    path('ipos/', views.IPOList.as_view(), name='ipo-list'),
    path('ipos/<int:pk>/', views.IPODetail.as_view(), name='ipo-detail'),
]
