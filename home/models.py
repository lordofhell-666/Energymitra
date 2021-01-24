from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime 

class Project(models.Model):
    title = models.CharField(max_length=100)
    s_date = models.DateTimeField(default=datetime.now, blank=True)
    client_name = models.CharField(max_length=100)
    Location = models.TextField()
    image = models.ImageField(upload_to='Projects/', null=True, blank=True)
    project_catg = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    about = models.TextField()
    slug = models.SlugField(blank=True , null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url

class Category(models.Model):
    name = models.CharField(max_length=100)  


    def __str__(self):
        return self.name  


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    download_link = models.CharField(max_length=100)
    description = models.TextField()
    feature_1 = models.CharField(max_length=100)
    feature_2 = models.CharField(max_length=100)
    feature_3 = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    d_price = models.CharField(max_length=100)
    slug = models.SlugField(blank=True , null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url


class email(models.Model):
    message = models.TextField()
