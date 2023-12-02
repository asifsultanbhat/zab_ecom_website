from django.db import models
from base.models import BaseModel
# Create your models here.


class Category(BaseModel):
  Category_name= models.CharField(max_length=100)
  slug =models.SlugField(unique=True, null=True, Blank=True)
  Category_image= models.ImageField(uploads="catgories")



class Product(BaseModel):
  Product_name = models.CharField(max_length=100)
  slug =models.SlugField(unique=True, null=True, Blank=True)
  Category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name= "products")
  prise = models.ImageField()
  product_descripation = models.TextField()



class ProductImage(BaseModel):
  product = models.ForeignKey(product,on_delete=models.CASCADE, related_name="product_image")
  image = models.ImageField(upload="product")