import requests.exceptions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView, FormView

from core.firebase_obj import pyre_database, pyre_auth
from core.models import Profile


class CreateUpdateView(
    SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView
):

    def get_object(self, queryset=None):
        try:
            return super(CreateUpdateView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).post(request, *args, **kwargs)


class ProfileView(CreateUpdateView):
    success_url = reverse_lazy("core:profile")
    model = Profile
    fields = ("phone_number", "company_name", "about_you")
    template_name = "profile/profile.html"

    def get_object(self, queryset=None):
        try:
            return self.request.user.profile
        except AttributeError:
            return None


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class LoginView(TemplateView):
    template_name = "account/login.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = pyre_auth.sign_in_with_email_and_password(email, password)
        except requests.exceptions.HTTPError as e:
            context = {
                "error":"Authentication Failed"
            }
            return render(request, "account/login.html", context)

        request.session["idToken"] = user["idToken"]
        print("hereeeeeeeeee")
        return redirect("core:profile")

