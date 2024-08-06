from django import forms
from .models import Tarea, SubTarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'style': 'width: 300px; height: 30px;'}),
        }

class SubTareaForm(forms.ModelForm):
    class Meta:
        model = SubTarea
        fields = ['descripcion', 'tarea']
        widgets = {
            'descripcion': forms.Textarea(attrs={'style': 'width: 300px; height: 30px;'}),
        }    