from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from dashboard.models import Category, Post, Notification

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	mobile = models.CharField(blank=True, max_length=13)
	device_id = models.CharField(blank=True, max_length=255)
	is_paid = models.BooleanField(default=False)
	fname = models.CharField(blank=True, max_length=50)
	lname = models.CharField(blank=True, max_length=50)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email


class UserPreference(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class UserBookmark(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


class UserNotification(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	notification_id = models.ForeignKey(Notification, on_delete=models.CASCADE)
