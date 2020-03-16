from django.db import models

class MetaData(models.Model):
	key = models.CharField(blank=False, max_length=255)
	value = models.TextField(blank=False)
	def __str__(self):
		return self.key


class UserDeviceData(models.Model):
	device_id = models.CharField(blank=False, max_length=255)
	firebase_id = models.CharField(blank=False, max_length=255)
	user_id = models.CharField(blank=False, max_length=255)