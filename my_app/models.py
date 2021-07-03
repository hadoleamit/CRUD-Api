from django.db import models

# Create your models here.


class Category(models.Model):
    PRODUCT_CHOICES =(
        ("CLOTHS", "Cloths"),
        ("VEGITABLE", "Vegitable"),
        ("BOOK", "Book")
    )
    category     = models.CharField(max_length=100,choices=PRODUCT_CHOICES)
    def __str__(self):
        return str(self.category)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category     = models.ForeignKey(Category, on_delete = models.CASCADE)
    price        = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

