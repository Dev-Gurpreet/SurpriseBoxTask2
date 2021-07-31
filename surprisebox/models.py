from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30,null=True, blank=True)
    is_winner = models.BooleanField(default=False)


 
