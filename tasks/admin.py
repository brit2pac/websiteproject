
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Position, Worker, TaskType, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class WorkerAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "position",
    )


admin.site.register(Worker, WorkerAdmin)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "task_type", "priority", "is_completed")
