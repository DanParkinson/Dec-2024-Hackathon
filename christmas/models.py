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
    title = models.CharField(max_length=200, unique=True)
    description = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)