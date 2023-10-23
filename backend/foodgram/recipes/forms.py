from django import forms
from spectrum.fields import ColorField
from .models import Tag


class TagForm(forms.ModelForm):
    color = forms.CharField(widget=ColorField)

    class Meta:
        model = Tag
        fields = '__all__'
