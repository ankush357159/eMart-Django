from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, default="", upload_to="images/")
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=0)
    stock = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=2)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')
    ratings = models.DecimalField(max_digits=3, decimal_places=1,null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title