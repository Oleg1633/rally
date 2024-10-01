from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
