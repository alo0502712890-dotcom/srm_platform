from django import forms
from django.forms import ModelForm
from .models import Comment, Task


class TaskRequestForm(ModelForm):

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'}
        )
    )

    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'assignee',
            'priority',
            'deadline',
        ]

        labels = {
            'title': 'Назва задачі',
            'description': 'Опис',
            'assignee': 'Виконавець',
            'priority': 'Пріоритет',
            'deadline': 'Дедлайн',
        }

        widgets = {
            'title': forms.TextInput(
                attrs={ 'placeholder': 'Введіть назву задачі'}
            ),

            'description': forms.Textarea(
                attrs={ 'rows': 6, 'placeholder': 'Опишіть задачу'}
            ),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']