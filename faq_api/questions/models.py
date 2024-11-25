from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_image = models.ImageField(upload_to='questions/', null=True, blank=True)
    answer_image = models.ImageField(upload_to='answers/', null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, related_name='faqs', on_delete=models.CASCADE, null=True, blank=True)