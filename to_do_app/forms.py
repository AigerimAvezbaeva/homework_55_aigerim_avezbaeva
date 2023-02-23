from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from to_do_app.models import ToDoParagraph


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoParagraph
        fields = ('title', 'description', 'status', 'completion_date')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title
