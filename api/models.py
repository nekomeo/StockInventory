from django.db import models

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=254, blank=True)
    quantity = models.IntegerField(blank=False)
    purchase_date = models.DateTimeField()
