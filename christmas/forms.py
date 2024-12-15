from django import forms
from .models import Recipe, CATEGORY_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from crispy_forms.layout import HTML

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'cooking_time', 'servings','image', 'category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'row g-3'  # Bootstrap 5 grid with gutters

        self.fields['instructions'].help_text = "Use 'Step 1: Do this. Step 2: Do that.' to separate your instructions."
        
        self.helper.layout = Layout(
            Div(
                Field('title', css_class='form-control'),
                css_class='col-md-12 mb-3'
            ),
            Div(
                Field('description', css_class='form-control'),
                css_class='col-md-12 mb-3'
            ),
            Div(
                Field('ingredients', css_class='form-control'),
                css_class='col-md-12 mb-3'
            ),
            Div(
                HTML("<small class='text-muted'>Use 'Step 1: Do this. Step 2: Do that.' to separate your instructions.</small>"),
                Field('instructions', css_class='form-control'),
                css_class='col-md-12 mb-3'
            ),
            Div(
                Field('cooking_time', css_class='form-control'),
                css_class='col-md-6 mb-3'
            ),
            Div(
                Field('image', css_class='form-control'),
                css_class='col-md-6 mb-3'
            ),
            Div(
                Field('category', css_class='form-select'),  # Bootstrap 5 select
                css_class='col-md-6 mb-3'
            ),
            Div(
                Field('servings', css_class='form-control'),  # New Servings Field
                css_class='col-md-6 mb-3'
            ),
            Div(
                Submit('submit', 'Save Recipe', css_class='btn btn-primary'),
                css_class='col-12'
            )
        )