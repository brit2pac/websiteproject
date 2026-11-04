
from django.urls import path

from tasks. import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tasks/create/", views.task_create, name="task-create"),
    path(
        "tasks/<int:pk>/toggle-completed/",
        views.task_toggle_completed,
        name="task-toggle-completed",
    ),
    path(
        "tasks/<int:pk>/edit/",
        views.task_update,
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        views.task_delete,
        name="task-delete",
    ),
    path("tasks/<int:pk>/", views.task_detail, name="task-detail"),
    path("workers/", views.worker_list, name="worker-list"),
    path(
        "workers/<int:pk>/",
        views.worker_detail,
        name="worker-detail",
    ),
    path("positions/", views.position_list, name="position-list"),
    path(
        "positions/<int:pk>/",
        views.position_detail,
        name="position-detail",
    ),
    path("task-types/", views.task_type_list, name="task-type-list"),
    path(
        "task-types/<int:pk>/",
        views.task_type_detail,
        name="task-type-detail",
    ),
]
