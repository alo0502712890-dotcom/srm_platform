from django.http import HttpResponse
from django.shortcuts import redirect


# 1 Головна
def home(request):
    return HttpResponse("<h1>CRM System</h1><p>Welcome!</p>")


# 2 задача по ID
def task_detail(request, task_id):
    return HttpResponse(f"<h2>Task ID: {task_id}</h2>")


# 3 фільтр задач
def task_list(request):
    status = request.GET.get('status')

    tasks = [
        {"id": 1, "title": "API", "status": "done"},
        {"id": 2, "title": "UI", "status": "in_progress"},
        {"id": 3, "title": "DB", "status": "todo"},
    ]

    if status:
        filtered = [t for t in tasks if t["status"] == status]
        return HttpResponse(f"Filtered tasks: {filtered}")

    return HttpResponse(f"All tasks: {tasks}")


# редірект на головну
def old_url(request):
    return redirect('/')


# http://127.0.0.1:8000/tasks/
# http://127.0.0.1:8000/tasks/2/
# http://127.0.0.1:8000/tasks/?status=done
# http://127.0.0.1:8000/old-url/

