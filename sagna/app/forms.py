from django import forms
from .models import Author, Publisher, Book, Customer, Order

from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'