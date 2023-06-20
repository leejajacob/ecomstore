from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField()

class order(models.Model):
    product=models.ForeignKey(Book,max_length=200,null=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
