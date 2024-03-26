from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date, timedelta

STATUS = (
    ('C', 'Complete'),
    ('I', 'Incomplete'),
)

# Create your models here.
class Goal(models.Model):
    title = models.TextField(max_length=250)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=date.today() + timedelta(days=1))
    status = models.CharField(
        max_length = 1,
        choices=STATUS,
        default=STATUS[1][0],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) #need this format for CP absolute url

    def get_absolute_url(self):
        return reverse('detail', kwargs={'goal_id': self.id})
    
class Checkpoint(models.Model):
    title = models.TextField(max_length=250)
    start_date = models.DateField(
        'checkpoint start date',
        default=timezone.now,
        )
    end_date = models.DateField(
        'checkpoint end date',
        default=date.today() + timedelta(days=1),
        )
    status = models.CharField(
        max_length = 1,
        choices=STATUS,
        default=STATUS[1][0],
    )
    status_color = models.TextField(
        max_length=40,
        default='red accent-3'
    )
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Checkpoint: {self.title} of goal ID {self.goal} (status: {self.get_status_display()})"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'goal_id': self.goal})
    
    class Meta:
        ordering = ['end_date']