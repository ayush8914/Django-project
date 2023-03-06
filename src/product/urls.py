from django.urls import path
from .import views

app_name = 'product'
urlpatterns =[
    path('',views.productlist ,name='product_list'),
    path('detail/<slug:product_slug>',views.productdetail, name='product_detail'),
    path('list/<slug:category_slug>',views.productlist, name='product_list_category'),
    path('post-ad/',views.postanad, name='postad'),
]