from django import forms
from .models import Book
from .models import Student, Address

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
