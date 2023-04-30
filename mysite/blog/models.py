from django.db import models
from django.db.models.query import QuerySet # Vem default, na criação da app
from django.utils import timezone # Usado no campo publish do Post, para considerar o timezone atual
from django.contrib.auth.models import User


## Gerenciadores de Modelo
class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')
                          
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts') # Esse é o nome da FK no banco
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-publish',)
    
    
    def __str__(self) -> str:
        return self.title
    