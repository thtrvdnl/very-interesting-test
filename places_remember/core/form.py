from .models import Place
from django.forms import ModelForm, TextInput, Textarea


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ("location", "comment")
        widgets = {
            "location": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий',
            }),
        }