from django.db import models

class Category(models.Model):
    '''Класс описывает категорию объявления'''
    name: str = models.CharField(max_length=200, unique=True)


class Advertsement(models.Model):
    '''Класс описывает объявление'''
    title: str = models.CharField(max_length=300)
    body: str = models.TextField()
    category: Category = models.OneToOneField("Category", on_delete=models.CASCADE)

