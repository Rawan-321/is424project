from django.db import models
from django.conf import settings

# Create your models here.

# missing user = models.ForeignKey(User, on_delete=models.CASCADE)
class Recipe(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    recipe_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipes", null=True)
    recipe_ingredients = models.CharField(max_length=400)
    recipe_description = models.TextField(max_length=400)
    instructions = models.TextField(default=None)
    cooking_time = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    recipe_image = models.ImageField(upload_to="images")


# missing user = models.ForeignKey(User, on_delete=models.CASCADE)
class Review(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

