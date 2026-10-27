
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task, TaskType, Worker


@login_required
def task_list(request):
    tasks = Task.objects.select_related("task_type").prefetch_related(
        "assignees"
    )

    query = request.GET.get("name")
    if query:
        tasks = tasks.filter(name__icontains=query)

    priority = request.GET.get("priority")
    if priority:
        tasks = tasks.filter(priority=priority)

    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        priority = request.POST.get("priority", "medium")
        task_type_id = request.POST.get("task_type")
        deadline = request.POST.get("deadline") or None
        assignee_ids = request.POST.getlist("assignees")

        if name and task_type_id:
            task = Task.objects.create(
                name=name,
                description=description,
                deadline=deadline,
                priority=priority,
                task_type_id=task_type_id,
            )
            task.assignees.set(assignee_ids)
            return redirect("task-list")

    return render(
        request,
        "tasks/task_form.html",
        {
            "task_types": TaskType.objects.all(),
            "workers": Worker.objects.all(),
            "priorities": Task.PRIORITY_CHOICES,
        },
    )

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        priority = request.POST.get("priority", "medium")
        task_type_id = request.POST.get("task_type")
        deadline = request.POST.get("deadline") or None
        assignee_ids = request.POST.getlist("assignees")

        if name and task_type_id:
            task.name = name
            task.description = description
            task.priority = priority
            task.task_type_id = task_type_id
            task.deadline = deadline
            task.save()
            task.assignees.set(assignee_ids)

            return redirect("task-list")

    return render(
        request,
        "tasks/task_form.html",
        {
            "task": task,
            "task_types": TaskType.objects.all(),
            "workers": Worker.objects.all(),
            "priorities": Task.PRIORITY_CHOICES,
        },
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
def task_toggle_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save(update_fields=["is_completed"])

    return redirect("task-list")