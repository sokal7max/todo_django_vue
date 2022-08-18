from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskView.as_view(), name='task_list_url'),
    path('<str:id>/complete/', TaskCmplete.as_view()),
    path('<str:id>/delete/', TaskDelete.as_view()),
]

