from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Access_Key(models.Model):
    key = models.CharField(max_length=254, unique=True)
    status = models.BooleanField(default=True)
    date_of_procurement =  models.DateTimeField()
    expiry_date = models.DateTimeField(auto_now_add=True)
    linked_institution = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def save(self, *args, **kwargs):
        if not self.expiry_date:  # Only set expiry_date if not already set
            self.expiry_date = timezone.now() + timedelta(days=365)
        super().save(*args, **kwargs)
