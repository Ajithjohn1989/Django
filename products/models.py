from django.db import models
from django.utils.text import slugify



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    image=models.ImageField(upload_to="product",default="product/book.jpg")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
