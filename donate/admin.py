from django.contrib import admin
from .models import Donation, Transaction
# Register your models here.

admin.site.register(Donation)

admin.site.register(Transaction)