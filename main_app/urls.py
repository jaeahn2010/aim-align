from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goals/', views.goals_index, name='index'),
    path('goals/<int:goal_id>/', views.goals_detail, name='detail'),
    path('goals/create/', views.GoalCreate.as_view(), name='goals_create'),
    path('goals/<int:pk>/update/', views.GoalUpdate.as_view(), name='goals_update'),
    path('goals/<int:pk>/delete/', views.GoalDelete.as_view(), name='goals_delete'),
    path('goals/<int:goal_id>/add_checkpoint/', views.add_checkpoint, name='add_checkpoint'),
]