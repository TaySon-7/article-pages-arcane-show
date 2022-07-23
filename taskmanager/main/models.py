from django.db import models
from django.urls import reverse



# Create your models here.
class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task= models.TextField("Описание")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Задача"
        verbose_name_plural ="Задачи"


class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug= models.CharField(max_length=255, unique=True )
    # is_published= models.BooleanField() #TODO
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Статья"
        verbose_name_plural ="Статьи"
    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug":self.slug})

