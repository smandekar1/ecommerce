
from products import views

from django.conf.urls import url

from .views import (
    ProductListView,
    product_list_view,
    RecentlyViewedView,
    ProductDetailSlugView, 

    )


urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^$', RecentlyViewedView.as_view(), name='recently_viewed'),

	# url(r'^$', views.product_list_view, name='list'),

    url(r'^(?P<slug>[\wi-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

]

