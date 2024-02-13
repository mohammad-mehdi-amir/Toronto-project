from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

    

class Image(models.Model):
    image=models.ImageField(upload_to='product_img')
    def __str__(self):
        return self.image.url
class Product(models.Model):
    title=models.CharField(max_length=120)
    price = models.IntegerField()
    inventory=models.IntegerField()
    status = models.BooleanField(default=True)
    # image=models.ForeignKey(Image,on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='product_img')
    image2=models.ImageField(upload_to='product_img',blank=True)
    image3=models.ImageField(upload_to='product_img',blank=True)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.PROTECT)
    
    datetime_add = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)
    #id
    def __str__(self):
        return self.title