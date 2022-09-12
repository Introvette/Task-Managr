from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=False)
    due_date = models.DateTimeField(null=False)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project", related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        "auth.User", related_name="tasks", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return str(self.name)
