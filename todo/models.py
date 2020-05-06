from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    def __str__(self):
        return self.name


class TasksModel(models.Model):
    todolist = models.ForeignKey(TodoModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
