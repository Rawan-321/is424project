from django import forms

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe Name', max_length=100)
    ingredients = forms.CharField(label='Ingredients', widget=forms.Textarea)
    instructions = forms.CharField(label='Instructions', widget=forms.Textarea)
    cooking_time = forms.IntegerField(label='Cooking Time (minutes)')
    image = forms.ImageField(label='Image')  # Optional field for image upload
    description = forms.CharField(label='Description', widget=forms.Textarea)  # Optional field for description