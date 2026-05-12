from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .forms import TaskRequestForm
from .models import Task



# Головна
def home(request):
    total_tasks = Task.objects.count()

    todo_tasks = Task.objects.filter(status='todo').count()
    in_progress_tasks = Task.objects.filter( status='in_progress').count()
    review_tasks = Task.objects.filter(status='review').count()
    done_tasks = Task.objects.filter( status='done').count()

    latest_tasks = Task.objects.order_by('-created_at')[:5]

    context = {
        'total_tasks': total_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
        'review_tasks': review_tasks,
        'latest_tasks': latest_tasks,
    }

    return render(request, 'srm_app/home.html', context)


# Список задач
def task_list(request):
    status = request.GET.get("status")

    tasks = Task.objects.all()

    if status:
        tasks = tasks.filter(status=status)

    context = {'tasks': tasks}

    return render(request, "srm_app/task_list.html", context)


# Деталі задачі
def task_detail(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id
    )

    context = {"task": task,}

    return render(request, "srm_app/task_detail.html", context)


# про нас
class AboutView(TemplateView):
    template_name = 'srm_app/about.html'

# формa
def create_task(request):
    if request.method == 'POST':
        form = TaskRequestForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = TaskRequestForm()

    context = {'form': form}
    return render(request,'srm_app/create_task.html',context)

# редірект
def old_url(request):
    return redirect('home')