from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product

def hello_world(request):
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	title = 'Productos en promocion'
	context = {
		'product': product,
		'title': title
	}
	return HttpResponse(template.render(context, request))
	#return HttpResponse('<h1> HELLO WORLD </h1>')
	
