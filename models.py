from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

class signupmodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username