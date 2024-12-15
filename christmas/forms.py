from django import forms
from .models import Recipe, CATEGORY_CHOICES

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'cooking_time', 'image', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
            'category': forms.Select(choices=CATEGORY_CHOICES),
        }