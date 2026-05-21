from rest_framework import serializers

from srm_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['id', 'title', 'description', 'assignee', 'deadline']