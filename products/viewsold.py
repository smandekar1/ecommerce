from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from carts.models import Cart
from .models import Product, ProductManager
from viewed_products.models import Viewed_Product, Viewed_Product_Manager
recently_viewed = []
prod_one = []
prod_two = []
prod_three = []
prod_four = [] 

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
        if instance not in recently_viewed:
            recently_viewed.insert(0,instance)

        # print('recently_viewed')
        # print(recently_viewed)

        # get or create session 

        viewed_product_obj, new_obj = Viewed_Product.objects.new_or_get(self.request)


        product_id = self.kwargs.get('slug')
        print('product_id is: ', product_id)

        Viewed_Product_Manager.foo()
       
        # product_id = request.POST.get('product_id')
        if product_id is not None:
            try:
                product_obj = Product.objects.get(slug=slug, active=True)
            except Product.DoesNotExist:
                print("Show message to user, product is gone?")
                return redirect("viewed_product:home")
            # if product_obj not in viewed_product_obj.products.all():
            # print('prod_obj was not in viewed_prod_objects...')
            # Viewed_Product.objects.add(product_obj)
            # viewed_objects = viewed_product_obj.products.last()
            # print('this viewed objects: ', viewed_objects)

            # global prod_two
            # if prod_two is not []:
            #     b = get_object_or_404(user=request.user, products=product_obj).delete()
            #     b = Viewed_Product.objects.filter(user=request.user, products=prod_two)
            #     del b
            global prod_one, prod_two

            if product_obj != prod_one and product_obj != prod_two:
                global prod_three 
                # if prod_three is not []:
                #     Viewed_Product.objects.remove(prod_three)
      
                prod_three = []

                # global prod_two
                prod_three = prod_two

                # global prod_one
                prod_two = prod_one    

                prod_one = product_obj

                print('prod_one: ', prod_one)
                print('prod_two: ', prod_two)
                print('prod_three: ', prod_three)                
                # if viewed_product_obj.products.count() == 1:
                #     print('viewed_product_obj.products.count() is 1')

                #     global prod_one 
                #     prod_one= product_obj
                #     # prod_two, prod_three, prod_four = [],[],[]
                #     print('prod_one: ', prod_one)

                # if viewed_product_obj.products.count() == 2:
                #     print('viewed_product_obj.products.count() is 2')

                    
                #     # global prod_one
                #     local_prod_two = prod_one
                #     global prod_two
                #     prod_two = local_prod_two
                #     # global prod_one
                #     prod_one = product_obj
                #     # prod_three, prod_four = [],[]
                #     print('prod_one: ', prod_one)
                #     print('prod_two: ', prod_two)

                # if viewed_product_obj.products.count() == 3:
                #     print('viewed_product_obj.products.count() is 3')

                    
                #     # global prod_one
                #     local_prod_three = prod_two
                #     global prod_three
                #     prod_three = local_prod_three
                #     # global prod_one
                #     local_prod_two = prod_one
                #     # global prod_two
                #     prod_two = local_prod_two
                #     prod_one = product_obj
                #     # prod_three, prod_four = [],[]
                #     print('prod_one: ', prod_one)
                #     print('prod_two: ', prod_two)
                #     print('prod_two: ', prod_three)
            

                # if viewed_product_obj.products.count() > 3:
                #     print('viewed_product_obj.products.count() is > 3')

                    
                #     # global prod_one
                #     local_prod_three = prod_two
                #     global prod_three
                #     prod_three = local_prod_three
                #     # global prod_one
                #     local_prod_two = prod_one
                #     # global prod_two
                #     prod_two = local_prod_two
                #     prod_one = product_obj
                #     # prod_three, prod_four = [],[]
                #     print('prod_one: ', prod_one)
                #     print('prod_two: ', prod_two)
                #     print('prod_two: ', prod_three)
            # # print('4 - THE OBJECT', product_obj)

            # if viewed_product_obj.products.count() > 2:
            #     # sprint(viewed_product_obj.products[0])
            #     print('before removing ', viewed_product_obj.products.all())
            #     print('removing: ', (viewed_product_obj.products.first()))
            #     viewed_product_obj.products.remove(viewed_product_obj.products.first())
            #     # first_element = viewed_product_obj.products.first()
            #     # print('first element', first_element)
            # print('5 - After', viewed_product_obj.products.all())
            
            # if viewed_product_obj.products.count() > 4:
            #     # print(viewed_product_obj.products[0])
            #     print('removing: ', (2, product_obj))
            #     viewed_product_obj.products.remove(2, product_obj)
            # print('5 - ALL PRODS', viewed_product_obj.products.all())

                # del viewed_product_obj.products[0]
                # viewed_product_obj.products.delete(product_obj)

        if product_id is None:
            print('product_id is None')        
            request.session['viewed_product_items'] = viewed_product_obj.products.count()
        print(' 7  - PORDUCT CoUNT')    
        print(len(viewed_product_obj.products))    
        # print(slug)
        # self.object = self.get_object() 
        # context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        # print(context)
        return instance


    def viewed_product_home(request):
        request = self.request   
        print('viewedeeee_product_obj')
        
        viewed_product_obj, new_obj = Viewed_Product.objects.new_or_get(self.request)

        # return render(request, "viewed_products/home.html", {"viewed_product": viewed_product_obj})
        print('viewed_product_obj')
        print(viewed_product_obj)

        return viewed_product_obj, new_obj


# connect session to user

# add this product to their session

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