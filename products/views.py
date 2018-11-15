from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from carts.models import Cart
from .models import Product, ProductManager

recently_viewed = []

class ProductFeaturedListView(ListView):
        template_name = "products/list.html"


        def get_queryset(self, *args, **kwargs):
            request = self.request
            return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
        queryset = Product.objects.all().featured() 
        template_name = "products/featured-detail.html"

 
        # def get_queryset(self, *args, **kwargs):
        #     request = self.request
        #     return Product.objects.featured()

class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print("fooo")
        return Product.objects.all()

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     print(recently_viewed)
    #     rec_view = "5"
    #     print("get_rec")
    #     return render(request, 'products/list.html', {'object_list': Product.objects.all(), 'rec_view': rec_view, 'recently_viewed': recently_viewed})
        # return (Product.objects.all(), {'recently_viewed': recently_viewed})
        # Product.objects.all(), 
        # return render(request, 'about.html', {'f':f,'form':form})
    
    def all(self):
        print("all")
        return self.get_queryset().active()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = recently_viewed
        # print(context['tags'].description)
        return context

def product_list_view(request):
    queryset = Product.objects.all()
    obj = [1,2,3]
    viewed_queryset = Product.objects.all()
    context = {
		'object_list': queryset,
        'viewed_list': viewed_queryset,
        'obj': obj,
    }
    return render(request, "products/list.html", context)

class RecentlyViewedView(ListView):
    template_name = "products/list.html"
    recently_viewed = recently_viewed

    # def get_queryset(self, recently_viewed):
    #     request = self.request
    #     print("fooll000000000000000l")
    #     return recently_viewed

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print("fooollllllll")
        return Product.objects.all()


def recently_viewed_view(request):
    queryset = Product.objects.all()
    context = {
        'reviewed_list': queryset 
    }
    return render(request, "products/recently_viewed.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self. request)
        context['cart'] = cart_obj

        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # item_id = Product.objects.get(pk=pk, active=True)
        # instance = get_object(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Foud..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm")
        # print(instance)
        if len(recently_viewed) > 3:
            del recently_viewed[-1]
        # global recently_viewed
        recently_viewed.insert(0,instance)
        # recently_viewed = instance + recently_viewed            
        # recently_viewed.append(instance)
        print(recently_viewed)

        # print(slug)
        # self.object = self.get_object() 
        # context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        # print(context)
        return instance

 

class ProductDetailView(DetailView):
# queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)

        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        # print(instance)

        if instance is None:
                raise Http404("Product Does Not Exist")
        return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
	# instance = Product.objects.get(pk=pk)
	# instance = get_object_or_404(Product, pk=pk)
    # try: 
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except: 
    #     print("huh?")
    instance = Product.objects.get_by_id(pk)
    # print(instance)
    if instance is None:
        raise Http404("Product Does Not Exist")

    # print(instance)



    # qs = Product.objects.filter(id=pk)
    # # print(qs  )

    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
	'object': instance
	}
    return render(request, "products/detail.html", context)