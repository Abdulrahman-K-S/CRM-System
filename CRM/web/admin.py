from django.contrib import admin
from . import models


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(models.Client)
class AdminClient(admin.ModelAdmin):
    pass