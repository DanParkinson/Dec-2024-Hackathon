from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

 
# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """ Model for recipes """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=100, unique=True)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes", default=30)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    favourites = models.ManyToManyField(User, related_name='favourite_recipes', blank=True)

    class Meta:
        """ 
        Orders recipies by:
        1. Recipes in draft.
        2. Oldest updated.
        i.e. shows oldest draft recipies which have not be published first.
        """
        ordering = ["status", "-updated_on"]


    def __str__(self):
        """Displays most useful recipe information."""
        return f"{self.status} | {self.author} | {self.title} | {self.description}"