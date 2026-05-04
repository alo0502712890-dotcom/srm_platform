from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

TASKS = [
    {
        "id": 1,
        "title": "API",
        "description": "Розробити API для CRM системи",
        "status": "done",
        "priority": "high",
        "assignee": "Олена",
        "deadline": datetime(2026, 5, 5),
        "comments": ["Зробити auth", "Додати CRUD"]
    },
    {
        "id": 2,
        "title": "UI",
        "description": "Створити інтерфейс користувача",
        "status": "in_progress",
        "priority": "medium",
        "assignee": "Іван",
        "deadline": datetime(2026, 5, 10),
        "comments": []
    },
    {
        "id": 3,
        "title": "DB",
        "description": "Налаштувати базу даних",
        "status": "todo",
        "priority": "high",
        "assignee": "Марія",
        "deadline": datetime(2026, 5, 8),
        "comments": ["Обрати PostgreSQL"]
    },
    {
        "id": 4,
        "title": "Auth",
        "description": "Реалізувати авторизацію",
        "status": "in_progress",
        "priority": "high",
        "assignee": "Олена",
        "deadline": datetime(2026, 5, 6),
        "comments": []
    },
    {
        "id": 5,
        "title": "Roles",
        "description": "Додати ролі користувачів",
        "status": "todo",
        "priority": "low",
        "assignee": "Андрій",
        "deadline": datetime(2026, 5, 12),
        "comments": []
    },
    {
        "id": 6,
        "title": "Dashboard",
        "description": "Зробити головну сторінку",
        "status": "done",
        "priority": "medium",
        "assignee": "Іван",
        "deadline": datetime(2026, 5, 3),
        "comments": []
    },
    {
        "id": 7,
        "title": "Notifications",
        "description": "Додати сповіщення",
        "status": "todo",
        "priority": "medium",
        "assignee": "Марія",
        "deadline": datetime(2026, 5, 15),
        "comments": []
    },
    {
        "id": 8,
        "title": "Search",
        "description": "Реалізувати пошук",
        "status": "in_progress",
        "priority": "low",
        "assignee": "Олена",
        "deadline": datetime(2026, 5, 11),
        "comments": []
    },
    {
        "id": 9,
        "title": "Filters",
        "description": "Додати фільтрацію",
        "status": "done",
        "priority": "medium",
        "assignee": "Андрій",
        "deadline": datetime(2026, 5, 4),
        "comments": []
    },
    {
        "id": 10,
        "title": "Deploy",
        "description": "Задеплоїти проект",
        "status": "todo",
        "priority": "high",
        "assignee": "Іван",
        "deadline": datetime(2026, 5, 20),
        "comments": []
    },
]


# Головна
def home(request):
    return render(request, "srm_app/home.html")


# Список задач + фільтр
def task_list(request):
    status = request.GET.get("status")

    if status:
        tasks = []

        for t in TASKS:
            if t["status"] == status:
                tasks.append(t)
    else:
        tasks = TASKS

    return render(request, "srm_app/task_list.html", {"tasks": tasks})


# Деталі задачі
def task_detail(request, task_id):
    task = None

    for t in TASKS:
        if t["id"] == task_id:
            task = t
            break

    if task is None:
        return HttpResponse("Task not found")

    context = {
        "task": task,
        "comments": task["comments"],
        "date": task["deadline"]
    }

    return render(request, "srm_app/task_detail.html", context)


# редірект
def old_url(request):
    return redirect('home')