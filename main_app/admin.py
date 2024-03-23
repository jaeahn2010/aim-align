from django.contrib import admin
from .models import Goal, Checkpoint

# Register your models here.
admin.site.register(Goal)
admin.site.register(Checkpoint)