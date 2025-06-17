from django.urls import path
from .views import PersonalityIndex

urlpatterns = [
    path('', PersonalityIndex.as_view())
]