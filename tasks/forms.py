from django import forms

from .models import Task, Worker


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        required=False,
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "task_type": forms.Select(attrs={"class": "form-select"}),
            "assignees": forms.SelectMultiple(
                attrs={"class": "form-select", "size": 5}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task_type"].empty_label = "Choose a type"
        self.fields["assignees"].queryset = Worker.objects.order_by("username")
