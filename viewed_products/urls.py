


from django.conf.urls import url

from .views import (
    viewed_product_home, 
    viewed_product_update, 

    )


urlpatterns = [

    url(r'^$', viewed_product_home, name='home'),
    url(r'^update/$', viewed_product_update, name='update'),

]

