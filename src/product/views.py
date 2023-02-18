from django.shortcuts import render
from .models import Product
# Create your views here.

def productlist(request):
    # to retrive all products from database
    productlist = Product.objects.all()    
    # print(productlist)

    
    template = 'Product/product_list.html'  
    context ={'product_list' : productlist} 
    return render(request,template,context)




def productdetail(request,id):
    print(id)
    productdetail = Product.objects.get(id=id)    
    # print(productlist)

    
    template = 'Product/product_detail.html'  
    context ={'product_details' : productdetail} 
    return render(request,template,context) 