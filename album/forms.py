from django import forms

from .models import AlbumM,mkSelectM
from django_summernote.widgets import SummernoteWidget

class CreateForm(forms.ModelForm):
    class Meta:
        model = AlbumM
        fields = ['title','category','name', 'age','explanation']
        widgets = {
            'explanation': SummernoteWidget(),
        }

class mkSelectForm(forms.ModelForm):
    class Meta:
        model=mkSelectM
        fields='__all__'
