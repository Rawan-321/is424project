from django.urls import path
from . import views

urlpatterns = [path("", views.recipe_screen_view, name='recipe'),
               path("addReview/", views.add_review, name="addReview")
               ]
