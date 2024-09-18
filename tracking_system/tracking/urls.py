from django.urls import path
from .views import NextTrackingNumber

urlpatterns = [
     path('next-tracking-number/', NextTrackingNumber.as_view(), name='next-tracking-number'),
]
