from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
	introduction = models.CharField(max_length=200, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now)
	fans = models.ManyToManyField(User, related_name='fans', blank=True)


	def __str__(self):
		return f'{ self.user.username } Profile'