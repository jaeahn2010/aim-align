from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Goal

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
    return render(request, 'goals/detail.html', { 'goal': goal })

class GoalCreate(CreateView):
    model = Goal
    fields = '__all__'

class GoalUpdate(UpdateView):
    model = Goal
    fields = '__all__'

class GoalDelete(DeleteView):
    model = Goal
    success_url = '/goals'