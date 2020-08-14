from django.db import models
from django.contrib.auth.models import User
from django.core import validators as v
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(
        max_length=200, 
        unique=True
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True
        )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='blog_posts'
        )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    content = models.TextField()
    created_on = models.DateTimeField(
        auto_now=True
    )
    status = models.IntegerField(
        choices=STATUS, 
        default=0
    )

class Authors(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        validators =[
            v.MinLengthValidator(3, 'Name should be 3 chars long'),
            v.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars')
        ]
    )
    email = models.CharField(
        max_length = 50,
        verbose_name = 'Email',
        unique = True,
        validators =[
            v.MinLengthValidator(5, 'Name should be 5 chars long'),
            v.MaxLengthValidator(50, 'Name shoild not be longer than 50 chars'),
            v.EmailValidator("Invalid Email")
        ]
    )

class Meta:
    ordering = ['-created_on']


