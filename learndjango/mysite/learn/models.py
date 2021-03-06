#coding:utf-8
from django.db import models
from learn.fields import ListField

# Create your models here.


class Person(models.Model):
     name = models.CharField(max_length=30)
     age = models.IntegerField()

     # 在Python3中使用 def __str__(self)
     def __unicode__(self):
        return self.name


class CustomFieldTest(models.Model):
    name = models.CharField(max_length=30)
    labels = ListField()

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.headline