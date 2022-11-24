
from django.urls import path, include
from .views import HelloAuthView, CustomUserCreateView


urlpatterns=[
    path('', HelloAuthView.as_view(), name='hello_auth'),
    path("signup/", CustomUserCreateView.as_view(), name="sign_up")
]