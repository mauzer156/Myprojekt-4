from django.urls import path
from .views import LoginCheckAPIView

urlpatterns = [
    path('login_check/', LoginCheckAPIView.as_view(), name='login_check'),
]
