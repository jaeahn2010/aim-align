from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Goal
from .forms import CheckpointForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def goals_index(request):
    goals = Goal.objects.all()
    return render(request, 'goals/index.html', {
        'goals': goals
    })

def goals_detail(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    checkpoint_form = CheckpointForm()
    return render(request, 'goals/detail.html', {
        'goal': goal,
        'checkpoint_form': checkpoint_form
    })

def add_checkpoint(request, goal_id):
    form = CheckpointForm(request.POST)
    if form.is_valid():
        new_checkpoint = form.save(commit=False)
        new_checkpoint.goal_id = goal_id
        new_checkpoint.save()
    return redirect('detail', goal_id=goal_id)

class GoalCreate(CreateView):
    model = Goal
    fields = ['title', 'start_date', 'end_date']

class GoalUpdate(UpdateView):
    model = Goal
    fields = ['title', 'start_date', 'end_date']

class GoalDelete(DeleteView):
    model = Goal
    success_url = '/goals'