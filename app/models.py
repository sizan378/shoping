from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATIC_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Faridpur','Faridpur'),
    ('Gazipur','Gazipur'),
    ('Gopalganj','Gopalganj'),
    ('Kishoreganj','Kishoreganj'),
    ('Madaripur','Madaripur'),
    ('Manikganj','Manikganj'),
    ('Munshiganj','Munshiganj'),
    ('Narayanganj','Narayanganj'),
    ('Narsingdi','Narsingdi'),
    ('Rajbari','Rajbari'),
    ('Shariatpur','Shariatpur'),
    ('Tangail','Tangail'),
    ('Bandarban','Bandarban'),
    ('Barhmanbaria','Barhmanbaria'),
    ('Chandpur','Chandpur'),
    ('Chattogram','Chattogram'),
    ("Cox's Bazar","Cox's Bazar"),
    ('Cumilla','Cumilla'),
    ('Feni','Feni'),
    ('Natore','Notore'),
    ('Pabna','Pabna'),

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATIC_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear')

)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    product_image = models.ImageField(upload_to='productimg')


    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES , default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 
