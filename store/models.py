from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.contrib.auth.models import User
# Using django's built-in User model

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # price = models.PositiveIntegerField() # price can be in floats so we will not use IntegerField here
    price = models.DecimalField(u'Price', decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    # u'Price' is unicode string so this field should be labeled as 'Price'. If any translation is applied to the site then
    # this label can be shown in other languages as well
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):

    # since enums are not supported using choices parameter for predefined values
    STATUS_CHOICES = [
        ('pending', 'Pending'), # (value stored in DB, human-readable label)
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted then delete the orders as well
    # created_at = models.DateTimeField(auto_now=True) # updates timestamp everytime you save
    created_at = models.DateTimeField(auto_now_add=True) # set timestamp once when created, doesnt change later
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    #                            ^ here max_length is for value not label
    total_price = models.DecimalField('Total', decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f"Order No. {self.id} by {self.user.username} - {self.status}"
    
    def update_total(self):
        total_stub = Decimal('0.0')
        for item in self.items.all():
            total_stub += item.product.price * item.quantity
        self.total_price = total_stub
        self.save()

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete= models.CASCADE, related_name='items') # related_name is like an alias
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def item_total(self):
        """
        This function will calculate the total for a single OrderItem
        """
        return self.product.price * self.quantity