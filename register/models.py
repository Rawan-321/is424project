from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from recipe.models import Recipe

# Create your models here.
class CustomUser(AbstractUser):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)

