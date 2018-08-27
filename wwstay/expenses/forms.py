from string import Template

from django import forms

from .models import Expense


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('title', 'description', 'price', 'image')
