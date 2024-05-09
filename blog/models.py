from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # status = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=options, default="draft")
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

"""
reverse(): Esto genera una URL a partir de un nombre de configuración de URL y un conjunto de argumentos.

get_absolute_url() sería la dirección específica que lleva a la vista detallada de un objeto en el sitio web, generada de manera dinámica y coherente con la estructura de URLs definida en el modelo.
"""
