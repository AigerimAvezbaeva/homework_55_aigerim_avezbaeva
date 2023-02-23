from django import forms
from to_do_app.models import ToDoParagraph


class ToDoForm(forms.Form):
    class Meta:
        model = ToDoParagraph
        fields = '__all__'

