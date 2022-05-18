from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse
import datetime
from workspace.models import Workspace
from django_quill.fields import QuillField

# Create your models here.


class Post(models.Model):
	"""model for Announcement"""
	# slug = models.SlugField(unique=True, null=False)
	title = models.CharField(max_length=150 )
	article = QuillField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse()
