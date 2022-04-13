"""Products models"""
from django.db import models
from profiles.models import UserProfile


class Category(models.Model):
    """Category model"""
    class Meta:
        """Meta class"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Friendly name def"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    "Product review model"
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'Review {self.review} by {self.author}'
