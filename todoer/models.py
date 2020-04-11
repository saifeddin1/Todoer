from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} Profile'

class Todo(models.Model):
	text = models.CharField(max_length=100)
	complete = models.BooleanField(default=False)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.text