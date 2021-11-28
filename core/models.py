from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser

app_label = "core"


class Profile(models.Model):
    phoneValidator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                      "'+999999999' or '987645321'. Up to 15 digits "
                                                                      "allowed.")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phoneValidator], max_length=17)
    company_name = models.CharField(max_length=100)
    about_you = models.TextField()

