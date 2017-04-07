from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone
class Counter(models.Model):
    hit_today = models.IntegerField(default=0)
    hit_total = models.IntegerField(default=0)
    hit_date  = models.DateTimeField()
    def publish(self):
        self.save()
    pass
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pass

class Bet(models.Model):
    TeamA = models.CharField(max_length=50)
    TeamB = models.CharField(max_length=50)
    BetSlip = models.CharField(max_length=50)
    Odds = models.CharField(max_length=50)
    BetAmount = models.CharField(max_length=50)

    def publish(self):
        self.save()
    def __str__(self):
        return self.title

