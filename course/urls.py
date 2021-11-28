from django.urls import path

from course import views

app_name = "course"

urlpatterns = [
    path("my_courses/", views.CourseListView.as_view(), name="my_courses" ),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="course_details"),
    path("create/", views.CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/create/", views.CourseVideoCreateView.as_view(), name="video_create"),
    path("courses/", views.AllCourseView.as_view(),name="all_courses"),
]