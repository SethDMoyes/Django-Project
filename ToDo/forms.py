from django.forms import ModelForm
from ToDo.models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model=ToDo
        fields="__all__"