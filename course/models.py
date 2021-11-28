from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
# Create your models here.
from course.misc_functions import video_upload_dir


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name="courses")
    name = models.CharField(max_length=256)
    description = models.TextField()


class CourseVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name="videos")
    course = models.ForeignKey(Course, models.CASCADE, related_name="videos")
    title = models.CharField(max_length=256)
    video = models.FileField(upload_to=video_upload_dir)

    def delete(self, *args, **kwargs):
        if self.video:  # If image isn't empty, delete image from storage
            storage, path = self.video.storage, self.video.path
            super(CourseVideo, self).delete(*args, **kwargs)
            storage.delete(path)
        else:
            super(CourseVideo, self).delete(*args, **kwargs)


class VideoProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name="progress")
    video = models.ForeignKey(CourseVideo, models.CASCADE, related_name="progress")
    progress = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])

    def set_progress(self, int):
        self.progress = max(min(int, 100), 0)
        self.save()