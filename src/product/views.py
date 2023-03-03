from django.shortcuts import render
from .models import Product,ProductImages,Category
from django.core.paginator import Paginator
from django.db.models import Count
# Create your views here.

def productlist(request):
    # to retrive all products from database
    productlist = Product.objects.all()    
    # print(productlist)
   
    Categorylist = Category.objects.annotate(total_products=Count('product'))
    template = 'Product/product_list.html'  
    paginator = Paginator(productlist, 1) # Show 25 contacts per page.
    # paginate_by = 1
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    context ={'product_list' : productlist,'category_list': Categorylist} 
    return render(request,template,context) 




def productdetail(request,product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)  
    productimages = ProductImages.objects.filter(product=productdetail)
    
    # print(productlist)

    
    template = 'Product/product_detail.html'  
    context ={'product_details' : productdetail,'product_images' : productimages} 
    return render(request,template,context) 