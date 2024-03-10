from django import forms
from .models import Category


class RecipeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    steps = forms.CharField(label='Steps', widget=forms.Textarea)
    cooking_time = forms.IntegerField(label='Cooking Time', min_value=1)
    image = forms.ImageField(label='Image', required=False)
    categories = forms.ModelMultipleChoiceField(label='Categories', queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
