from django import forms
from course.models import CourseVideo

class CourseVideoCreateForm(forms.ModelForm):
    model = CourseVideo