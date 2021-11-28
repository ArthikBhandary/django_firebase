from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

from core.models import Profile


class CreateUpdateView(
    LoginRequiredMixin, SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView
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

