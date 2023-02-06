from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/new.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        project_id = self.object.project.id
        return reverse_lazy("show_project", kwargs={"pk": project_id})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
