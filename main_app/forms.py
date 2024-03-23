from django.forms import ModelForm
from .models import Checkpoint

class CheckpointForm(ModelForm):
    class Meta:
        model = Checkpoint
        fields = ['title', 'start_date', 'end_date']