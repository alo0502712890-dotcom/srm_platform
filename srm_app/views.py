from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskRequestForm
from .forms import CommentForm
from .models import Task, Comment


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
@login_required
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

@login_required
def dashboard(request):
    tasks = Task.objects.filter(assignee=request.user.username)
    total_tasks = tasks.count()
    todo_tasks = tasks.filter(status='todo').count()
    in_progress_tasks = tasks.filter(status='in_progress').count()
    review_tasks = tasks.filter(status='review').count()
    done_tasks = tasks.filter(status='done').count()


    latest_tasks = tasks.order_by('-created_at')[:5]
    comments = Comment.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'review_tasks': review_tasks,
        'done_tasks': done_tasks,
        'latest_tasks': latest_tasks,
        'comments': comments,
    }

    return render(request,'srm_app/dashboard.html',context)


@login_required
def task_detail(request, task_id):

    task = get_object_or_404(Task,id=task_id)

    # Зміна статусу
    if request.method == 'POST' and 'status' in request.POST:
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('task_detail',task_id=task.id)

    # Додавання коментаря
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            already_exists = Comment.objects.filter(
                task=task,
                user=request.user,
                text=text
            ).exists()

            if already_exists:
                form.add_error('text','Такий коментар уже існує')

            else:
                comment = form.save(commit=False)
                comment.task = task
                comment.user = request.user
                comment.save()

                return redirect('task_detail',task_id=task.id)
    else:
        form = CommentForm()

    context = {'task': task,'form': form}

    return render(request,'srm_app/task_detail.html',context)