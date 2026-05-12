from django import forms


class TaskRequestForm(forms.Form):

    title = forms.CharField(min_length=3,max_length=100,label='Назва задачі')
    assignee = forms.CharField(min_length=2,max_length=50,label='Виконавець')
    description = forms.CharField(widget=forms.Textarea,min_length=10,label='Опис')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'test' in title.lower():
            raise forms.ValidationError(
                'Назва не може містити "test"'
            )
        return title