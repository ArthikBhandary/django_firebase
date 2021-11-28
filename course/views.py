from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from course.models import Course, CourseVideo


class CourseCreateView(LoginRequiredMixin, CreateView):
    template_name = "course/courses_create.html"
    model = Course
    fields = ["name", "description"]

    def get_success_url(self):
        print("SUCCESS")
        return reverse_lazy("course:course_details", kwargs={"pk":self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CourseListView(LoginRequiredMixin, ListView):
    template_name = "course/courses.html"

    def get_queryset(self):
        return self.request.user.courses


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "course/course_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AllCourseView(LoginRequiredMixin, ListView):
    template_name = "course/all_courses.html"
    model = Course


class CourseVideoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "course/video_create.html"
    model = CourseVideo
    fields = ("title", "video")

    def get_success_url(self):
        return reverse_lazy("course:course_details", pk=self.kwargs["pk"])

    def has_permission(self):
        course = get_object_or_404(Course, pk=self.kwargs["pk"])
        return course.user == self.request.user

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.course = get_object_or_404(Course, pk=self.kwargs["pk"])
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class VideoDetailsView(LoginRequiredMixin, DetailView):
    template_name = "course/video.html"
    model = CourseVideo
