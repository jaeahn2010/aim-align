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
    path('checkpoints/<int:pk>/update/', views.CheckpointUpdate.as_view(), name='checkpoints_update'),
    path('checkpoints/<int:pk>/delete/', views.CheckpointDelete.as_view(), name='checkpoints_delete'),
    path('checkpoints/<int:checkpoint_id>/update_status/', views.checkpoints_update_status, name='checkpoints_update_status'),
    path('accounts/signup/', views.signup, name='signup'),
]