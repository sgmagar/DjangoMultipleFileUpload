from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Person
        fields = [
            'name',
            'age',
        ]