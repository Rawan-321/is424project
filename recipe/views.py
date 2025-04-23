from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from recipe.models import Recipe, Review

# Create your views here.


def recipe_screen_view(request):
    total_reviews = 0
    context = {}
    recipe1 = Recipe.objects.get(pk=1)
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


def add_review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        # user = request.user
        recipe_id = request.POST.get('recipe_id')
        recipe = Recipe.objects.get(pk=recipe_id)

        review_instance = Review(content=review, recipe_name=recipe)
        review_instance.save()
        messages.success(request, "review added successfully!")
    else:
        messages.error(request,"An error while adding review!")

    return redirect('recipe')





