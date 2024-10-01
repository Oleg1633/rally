from django.contrib import admin
from . import models
  
@admin.register(models.Team) 
class TeamAdmin(admin.ModelAdmin): 
    list_display = ['name']# [field.name for field in models.Team._meta.get_fields()]


@admin.register(models.Pilot) 
class PilotAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Pilot._meta.get_fields()]