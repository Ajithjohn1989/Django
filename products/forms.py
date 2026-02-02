from django import forms
from .models import Category,Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =[
            'category',
            'author',
            'price',
            'description',
            'title',
            'image',
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'name',
            'description',
        ]



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'title',
            'author',
            'description',
            'price',
            'is_active',
            'image',
        ]