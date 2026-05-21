from django.contrib import admin
from srm_app.models import Task, Comment, Profile

# Register your models here.

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Profile)