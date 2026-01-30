from django.urls import path
from products import views

app_name="products"

urlpatterns=[
    path("add-category",views.add_category,name="add_category"),
    path("add-product",views.add_product,name="add_product")

]