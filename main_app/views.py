from django.shortcuts import render

# mock data
goals = [
    {
        'id': 1,
        'title': 'finish project',
        'start_date': '2024-03-22',
        'end_date': '2024-03-29',
    },
    {
        'id': 2,
        'title': 'finish housework',
        'start_date': '2024-03-22',
        'end_date': '2024-03-24',
    },
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def goals_index(request):
    return render(request, 'goals/index.html', {
        'goals': goals
    })