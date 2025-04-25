from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from recipe.models import Recipe, Review
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def recipe_screen_view(request,id):
    total_reviews = 0
    context = {}
    recipe1 = Recipe.objects.get(pk=id)
    reviews = Review.objects.filter(recipe_name=recipe1).order_by("created_at")
    for i in range(len(reviews)):
        total_reviews += 1
    context['recipe'] = recipe1
    context['reviews'] = reviews
    context['total_reviews'] = total_reviews
    context['ingredients'] = recipe1.recipe_ingredients.split(',')
    context['instructions'] = recipe1.instructions.split('\n')
    # last argument is for context if you have data you will get from the db
    return render(request, 'recipe/recipe.html', context)



@login_required
def add_review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        # user = request.user
        recipe_id = request.POST.get('recipe_id')
        recipe = Recipe.objects.get(pk=recipe_id)

        review_instance = Review(content=review, recipe_name=recipe)
        review_instance.user = request.user
        review_instance.save()
        messages.success(request, "review added successfully!")
    else:
        messages.error(request,"An error while adding review!")

    return redirect('recipe_view', id=recipe_id)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
            recipe_ingredients = form.cleaned_data['ingredients']
            recipe_description = form.cleaned_data['description']
            instructions = form.cleaned_data['instructions']
            cooking_time = form.cleaned_data['cooking_time']
            recipe_image = form.cleaned_data['image']

            recipe_instance = Recipe(
            recipe_name=recipe_name,
            recipe_ingredients=recipe_ingredients,
            recipe_description=recipe_description,
            instructions=instructions,
            cooking_time=cooking_time,
            recipe_image=recipe_image)
            recipe_instance.user = request.user
            recipe_instance.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_view", id=recipe_instance.id)
        else:
            messages.error(request, "Form is not valid!")
            
    else:
        form = RecipeForm()

    return render(request, 'recipe/add.html', {'form': form})


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, "recipe/home.html", context)


