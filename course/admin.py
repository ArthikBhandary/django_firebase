from django.contrib import admin

# Register your models here.
from course.models import Course, CourseVideo

admin.site.register(Course)
admin.site.register(CourseVideo)