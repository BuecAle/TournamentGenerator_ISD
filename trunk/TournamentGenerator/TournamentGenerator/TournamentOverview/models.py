from django.db import models
from django.urls import reverse

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    summary = models.TextField(default="This is a default value")
    features = models.BooleanField(default="True")

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"my_id" : self.id})


