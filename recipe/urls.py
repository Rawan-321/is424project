from django.urls import path
from . import views

urlpatterns = [path("home/recipe/<int:id>/", views.recipe_screen_view, name='recipe_view'),
               path("addReview/", views.add_review, name="addReview"),
               path("home/",view=views.home, name="home"),
               path("createRecipe/", view=views.create_recipe, name="createRecipe")
               ]
