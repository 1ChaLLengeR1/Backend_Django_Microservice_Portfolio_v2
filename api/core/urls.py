from django.urls import path
from core.views.user import get_user_view
from core.views.home.one import view_one_home

urlpatterns = [
    path('user/', get_user_view),
    path('home', view_one_home),
]
