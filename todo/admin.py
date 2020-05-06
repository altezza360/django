from django.contrib import admin
from .models import TodoModel, TasksModel

admin.site.register(TodoModel)
admin.site.register(TasksModel)
