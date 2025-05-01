from django.urls import path
from api.views import get_user_view

urlpatterns = [
    path('user/', get_user_view),
]
