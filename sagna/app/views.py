from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Publisher, Book, Customer, Order
from .forms import AuthorForm, PublisherForm, BookForm, CustomerForm, OrderForm,Publisher
from .forms import AuthorForm
from .models import Author  

def index_page(request):
    return render(request, 'pages/index.html')

def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def login_page(request):
    return render(request, 'pages/login.html')




def author_list(request):
    authors = Author.objects.all()
    return render(request, 'pages/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'pages/author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'pages/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'pages/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'pages/author_confirm_delete.html', {'author': author})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'pages/publisher_list.html', {'publishers': publishers})
def book_list(request):
    books = Book.objects.all()
    return render(request, 'pages/book_list.html', {'books': books})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'pages/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pages/order_list.html', {'orders': orders})