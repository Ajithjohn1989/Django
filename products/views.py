from django.shortcuts import render,redirect,get_object_or_404
from .forms import CategoryForm,ProductForm
from products.models import Category,Product


from django.http import HttpResponse
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("New category added")
        
    else:
        form = CategoryForm()
    return render(request,'category/add_category.html',{'form':form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("New Product Added!")

    else:
        form = ProductForm()
    cat=Category.objects.all()
    return render(request,'products/add_books.html', {'form': form,"categories":cat})



def edit_book(request, id):
    book = get_object_or_404(Product, id=id)   

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ProductForm(instance=book)

    return render(request, 'products/edit_books.html', {'form': form})
