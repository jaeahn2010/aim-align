from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import date, timedelta

# Create your models here.
class Goal(models.Model):
    title = models.TextField(max_length=250)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=date.today() + timedelta(days=1))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'goal_id': self.id})