from django import forms
from .models import *

class counterForm(forms.ModelForm):
    class Meta:
        model = Counter_app
        fields = ('number',)
