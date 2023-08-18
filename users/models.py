from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image=models.ImageField(upload_to='images', null=True)
    address= models.CharField(max_length=255 )
    telephone=models.CharField(max_length=12)

    def __str__(self) -> str:
        return f' {self.user.username}'