from django.db import models


class User(models.Model):
    login_name = models.CharField(primary_key = True, max_length = 254) # max email address length
    nickname = models.CharField(max_length = 64)
    registration_datetime = models.DateTimeField()

class Chore(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    is_done = models.BooleanField(default = False)
    creation_datetime = models.DateTimeField()
    chore_text = models.CharField(max_length = 256)