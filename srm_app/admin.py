from django.contrib import admin
from srm_app.models import Task, Comment

# Register your models here.

admin.site.register(Task)
admin.site.register(Comment)