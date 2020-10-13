from django.db import models

# Create your models here.

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length = 40)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    product_image = models.ImageField(upload_to="Product")
    product_name = models.CharField(max_length = 30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    preview_text = models.TextField(max_length=200,verbose_name='preview_text')
    details = models.TextField(max_length=1000,verbose_name='details')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name)


    class Meta:
        ordering = ["created"]
