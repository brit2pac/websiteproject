
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from tasks.forms import TaskForm
from tasks.models import Position, Task, TaskType, Worker


@login_required
def task_list(request):
    tasks = (
        Task.objects
        .select_related("task_type")
        .prefetch_related("assignees")
    )

    query = request.GET.get("name")
    if query:
        tasks = tasks.filter(name__icontains=query)

    priority = request.GET.get("priority")
    if priority:
        tasks = tasks.filter(priority=priority)

    status = request.GET.get("status")
    if status == "completed":
        tasks = tasks.filter(is_completed=True)
    elif status == "open":
        tasks = tasks.filter(is_completed=False)

    tasks = tasks.order_by("deadline", "pk")
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": page_obj,
            "page_obj": page_obj,
            "priorities": Task.PRIORITY_CHOICES,
        },
    )


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("task-list")

    return render(
        request,
        "tasks/task_form.html",
        {"form": form},
    )


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("task-detail", pk=task.pk)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "task": task},
    )


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task-list")

    return render(
        request,
        "tasks/task_confirm_delete.html",
        {"task": task},
    )


@login_required
@require_POST
def task_toggle_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])
    return redirect("task-list")


@login_required
def worker_list(request):
    workers = Worker.objects.select_related("position").all()

    return render(
        request,
        "tasks/worker_list.html",
        {"workers": workers},
    )


@login_required
def worker_detail(request, pk):
    worker = get_object_or_404(
        Worker.objects.select_related("position"),
        pk=pk,
    )

    tasks = (
        worker.tasks
        .select_related("task_type")
        .order_by("deadline", "name")
    )

    return render(
        request,
        "tasks/worker_detail.html",
        {
            "worker": worker,
            "open_tasks": tasks.filter(is_completed=False),
            "completed_tasks": tasks.filter(is_completed=True),
        },
    )


@login_required
def position_list(request):
    positions = Position.objects.all()

    return render(
        request,
        "tasks/position_list.html",
        {"positions": positions},
    )


@login_required
def position_detail(request, pk):
    position = get_object_or_404(Position, pk=pk)
    workers = Worker.objects.filter(position=position)

    return render(
        request,
        "tasks/position_detail.html",
        {
            "position": position,
            "workers": workers,
        },
    )


@login_required
def task_type_list(request):
    task_types = TaskType.objects.all()

    return render(
        request,
        "tasks/task_type_list.html",
        {"task_types": task_types},
    )


@login_required
def task_type_detail(request, pk):
    task_type = get_object_or_404(TaskType, pk=pk)
    tasks = Task.objects.filter(task_type=task_type)

    return render(
        request,
        "tasks/task_type_detail.html",
        {
            "task_type": task_type,
            "tasks": tasks,
        },
    )


@login_required
def task_detail(request, pk):
    task = get_object_or_404(
        Task.objects
        .select_related("task_type")
        .prefetch_related("assignees"),
        pk=pk,
    )

    return render(
        request,
        "tasks/task_detail.html",
        {"task": task},
    )
