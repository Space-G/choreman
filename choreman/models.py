import datetime

from django.db import models


class User(models.Model):
    """TODO: learn about Django's auth module. That's why there's nothing like a "hashed password" field"""
    login_name = models.CharField("username used to login", primary_key = True, max_length = 254) # max email address length
    nickname = models.CharField("name shown", max_length = 64)
    registration_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.login_name} {self.nickname} {self.registration_datetime.isoformat(' ')}"

class Chore(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    is_done = models.BooleanField(default = False)
    creation_datetime = models.DateTimeField()
    chore_description = models.CharField(max_length = 256)

    def __str__(self):
        return f"{self.creation_datetime.isoformat(' ')}\t{self.creator.login_name} ({self.creator.nickname})\t{'✔' if self.is_done else '❌'}\t{self.chore_description}"