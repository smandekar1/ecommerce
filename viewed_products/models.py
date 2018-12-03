

from django.conf import settings
from django.db import models
# from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product


User = settings.AUTH_USER_MODEL

class Viewed_Product_Manager(models.Manager):
    def new_or_get(self, request):
        viewed_product_id = request.session.get("viewed_product_id", None)
        qs = self.get_queryset().filter(id=viewed_product_id)
        if qs.count() == 1:
            new_obj = False
            viewed_product_obj = qs.first()
            if request.user.is_authenticated and viewed_product_obj.user is None:
                viewed_product_obj.user = request.user
                viewed_product_obj.save()
        else:
            viewed_product_obj = Viewed_Product.objects.new(user=request.user)
            new_obj = True
            request.session['viewed_product_id'] = viewed_product_obj.id
        return viewed_product_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Viewed_Product(models.Model):
    user        = models.ForeignKey(User,  on_delete=models.CASCADE, null=True, blank=True)
    # products    = models.SlugField(Product, blank=True)
    # products    = models.CharField(max_length=200)
    products    = models.ManyToManyField(Product, blank=True)

    

	# slug 		= models.SlugField(blank=True, unique=True)

    # subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    # total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    # updated     = models.DateTimeField(auto_now=True)
    # timestamp   = models.DateTimeField(auto_now_add=True)

    objects = Viewed_Product_Manager()

    # def __str__(self):
    #     return str(self.id)
















