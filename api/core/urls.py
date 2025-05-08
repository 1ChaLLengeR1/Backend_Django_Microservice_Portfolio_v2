from django.urls import path
from core.views.user import get_user_view

urlpatterns = [
    path('user/', get_user_view),
]
