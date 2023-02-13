from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    CONDITION_TYPE = (
        ("New" , "New"),
        ("Used", "Used")
    )
    ## contains all the product info
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    Brand = models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        #to see product name in admin site
        return self.name
    
class Category(models.Model):
        ##for product category
        
        category_name = models.CharField(max_length=50)
        image = models.ImageField(upload_to='products/',blank=True, null=True)
        
        class Meta:
            verbose_name = 'category'
            verbose_name_plural = 'categories'
            
        def __str__(self):
        #to see product name in admin site
          return self.category_name
      
class Brand(models.Model):
        ##for product brand
        
        brand_name = models.CharField(max_length=50)
        # image = models.ImageField(upload_to='products/',blank=True, null=True)
        
        class Meta:
            verbose_name = 'brand'
            verbose_name_plural = 'brands'
            
        def __str__(self):
        #to see product name in admin site
          return self.brand_name