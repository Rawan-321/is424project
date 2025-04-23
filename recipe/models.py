from django.db import models

# Create your models here.

# missing user = models.ForeignKey(User, on_delete=models.CASCADE)
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=40)
    recipe_ingredients = models.CharField(max_length=400)
    recipe_description = models.TextField(max_length=400)
    instructions = models.TextField(default=None)
    cooking_time = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    recipe_image = models.ImageField(upload_to="images")


# missing user = models.ForeignKey(User, on_delete=models.CASCADE)
class Review(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

