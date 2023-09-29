from django.contrib import admin
from.models import productmodel 
from django import forms

# Register your models here.
class ProductForm(forms.ModelForm):
	class Meta:
		model=productmodel
		fields= '__all__'
