from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FriendGroup(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField(User)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_model")


class Collection(models.Model):
    name = models.CharField(max_length=100, default="")
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print("SAVING")
        models.Model.save(self, *args, **kwargs)


class FriendInstance(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_paid = models.BooleanField()
