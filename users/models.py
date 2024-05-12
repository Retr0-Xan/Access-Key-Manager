from django.db import models
from access_keys.models import Access_Key
# Create your models here.

class User(models.Model):
    institution_email = models.EmailField(max_length=254)
    institution_name = models.CharField(max_length=254)
    linked_access_key= models.ForeignKey(Access_Key, on_delete=models.CASCADE,default=None)
    key = models.BooleanField(default=True)
