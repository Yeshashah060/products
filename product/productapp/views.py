from django.shortcuts import render , redirect
from.models import productmodel
from.forms import ProductForm

# Create your views here.
def homepage(request):
	if request.method == "POST":
		product_form = ProductForm(request.POST)
		if product_form.is_valid():
			product_form.save()
		return redirect(homepage)

	product_form = ProductForm()
	product = productmodel.objects.all()
	context = {'product_form':product_form, 'product':product}
	return render(request, 'Home.html', context)

