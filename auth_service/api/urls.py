from django.urls import path
from auth_service.api.views.user import get_user_view

urlpatterns = [
    path('user/', get_user_view),
]
