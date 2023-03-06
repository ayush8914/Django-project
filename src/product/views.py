from django.shortcuts import render
from .models import Product,ProductImages,Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from .forms import UserForm
# Create your views here.

def productlist(request , category_slug=None):
    category=None
    # to retrive all products from database
    productlist = Product.objects.all()    
    # print(productlist)
   
    Categorylist = Category.objects.annotate(total_products=Count('product'))
    
    if category_slug :
        category = Category.objects.get(slug=category_slug)
        productlist = productlist.filter(category=category)
        
    search_query = request.GET.get('q')
    if search_query:
      productlist = productlist.filter(
          Q(name__icontains = search_query) |
          Q(description__icontains = search_query) |
          Q(condition__icontains = search_query) |
          Q(Brand__brand_name__icontains = search_query) |
          Q(category__category_name__icontains =search_query)
      )
    
    
    template = 'Product/product_list.html'  
    paginator = Paginator(productlist, 2) # Show 25 contacts per page.
    # paginate_by = 1
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    context ={'product_list' : productlist,'category_list': Categorylist,'category':category} 
    return render(request,template,context) 




def productdetail(request,product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)  
    productimages = ProductImages.objects.filter(product=productdetail)
    
    # print(productlist)

    
    template = 'Product/product_detail.html'  
    context ={'product_details' : productdetail,'product_images' : productimages} 
    return render(request,template,context) 

def postanad(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/products')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

   
    template = 'Product/post-ad.html'  
    return render(request,template,context)