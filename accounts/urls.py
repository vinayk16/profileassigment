from django.urls import path, include
from accounts.views import UserProfileAPIView

urlpatterns = [
    path('profiles/', UserProfileAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>', UserProfileAPIView.as_view(), name='profiles'),
]
