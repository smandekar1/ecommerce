
from django.shortcuts import render, redirect

from products.models import Product
from .models import Viewed_Product

def viewed_product_home(request):
    viewed_product_obj, new_obj = Viewed_Product.objects.new_or_get(request)

    return render(request, "viewed_products/home.html", {"viewed_product": viewed_product_obj})


def viewed_product_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show message to user, product is gone?")
			return redirect("viewed_product:home")
		viewed_product_obj, new_obj = Viewed_Product.objects.new_or_get(request)
		if product_obj in viewed_product_obj.products.all():
			viewed_product_obj.products.remove(product_obj)
		else:
			viewed_product_obj.products.add(product_obj)
		request.session['reviewed_product_items'] = reviewed_product_obj.products.count()
	
	# return redirect(product_obj.get_absolute_url())
	return redirect("reviewed_product:home")