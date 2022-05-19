from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Transaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.IntegerField(blank=True, null=True)
	status = models.BooleanField(default=False)



class Donation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=200, blank=True, null=True)
	amount = models.IntegerField(blank=True, null=True)
	donated_at = models.DateTimeField(default=timezone.now)
	donated_to = models.ForeignKey(User, on_delete= models.CASCADE, related_name='creator', blank=True)


	def __str__(self):
		return f'{ self.user.username } Profile'


