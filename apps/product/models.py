from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='image/', null=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField('Доступно', default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', to_field='name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/image/')

    def __str__(self):
        return self.product.name
