from django.db import models
from django.urls import reverse

# Create your models here.
class Goal(models.Model):
    title = models.TextField(max_length=250)
    start_date = models.DateField
    end_date = models.DateField

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'goal_id': self.id})