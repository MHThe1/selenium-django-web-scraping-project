from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Board(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_link = models.CharField(max_length=400)


    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super(Board, self).save(*args, **kwargs)

    def verify_password(self, raw_password):
        # Check if the provided raw password matches the hashed password
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.created_at} - {self.updated_at}"


class Stat(models.Model):
    parent_id = models.PositiveSmallIntegerField()
    ign = models.CharField(max_length=30)
    matches = models.PositiveSmallIntegerField()
    kills = models.PositiveSmallIntegerField()
    damage = models.PositiveSmallIntegerField()
    knocks = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()
    longest = models.PositiveSmallIntegerField()
    travel = models.PositiveSmallIntegerField()
    revives = models.PositiveSmallIntegerField()
    accuracy = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id} - {self.ign} - {self.kills} - {self.damage}"
