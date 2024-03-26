from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Goal, Checkpoint
from .forms import CheckpointForm
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up. Try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def goals_index(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/index.html', {
        'goals': goals
    })

@login_required
def goals_detail(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    checkpoint_form = CheckpointForm()
    return render(request, 'goals/detail.html', {
        'goal': goal,
        'checkpoint_form': checkpoint_form
    })

@login_required
def add_checkpoint(request, goal_id):
    form = CheckpointForm(request.POST)
    if form.is_valid() and request.POST['start_date'] <= request.POST['end_date']:
        goal = Goal.objects.get(pk=goal_id)
        checkpoint_start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
        checkpoint_end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
        if goal.start_date <= checkpoint_start_date and goal.end_date >= checkpoint_end_date:
            new_checkpoint = form.save(commit=False)
            new_checkpoint.goal_id = goal_id
            new_checkpoint.save()
        else:
            messages.error(request, 'Checkpoint date range must be within the goal date range.')
    else:
        messages.error(request, 'End date must be set after start date.')
    return redirect('detail', goal_id=goal_id)

@login_required
def checkpoints_update_status(request, checkpoint_id):
    checkpoint = Checkpoint.objects.get(pk=checkpoint_id)
    goal = Goal.objects.get(pk=checkpoint.goal_id)
    checkpoint.status = 'C'
    checkpoint.status_color = 'green'
    checkpoint.save()
    return render(request, 'goals/detail.html', {
        'goal': goal,
    })

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['title', 'start_date', 'end_date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['title', 'start_date', 'end_date']

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    success_url = '/goals'

class CheckpointUpdate(LoginRequiredMixin, UpdateView):
    model = Checkpoint
    fields = ['title', 'start_date', 'end_date']

class CheckpointDelete(LoginRequiredMixin, DeleteView):
    model = Checkpoint
    success_url = f"/goals"