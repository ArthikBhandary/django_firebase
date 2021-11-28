
from django.urls import path

from core import views
# from allauth.account.views import LoginView

app_name = "core"

urlpatterns = [
    path("home/", views.ProfileView.as_view(), name="profile"),
    path("", views.LoginView.as_view(), name="login"),
]