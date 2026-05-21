from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from srm_app.models import Task
from srm_app.serializers import TaskSerializer


@api_view(["GET"])
def task_list_api(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)