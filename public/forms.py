from django import forms
from public.models import Public

class PublicForm(forms.ModelForm):
    class Meta:
        model=Public
        fields=['title', 'description', 'cat_id']