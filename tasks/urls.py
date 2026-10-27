
from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tasks/create/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task-update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path(
    "tasks/<int:pk>/toggle-completed/",
    views.task_toggle_completed,
    name="task-toggle-completed",
    ),
]
