import decimal

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class authUser(User):
    iin = models.CharField(max_length=12)
    is_renter = models.BooleanField(default=False)
    num_tel = models.CharField(max_length=15)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product-img/', default='product-img/pro-big-1.jpg')
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Item, blank=True)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.products.count(),
                                                                                self.total)

    def get_total_price(self):
        return sum(self.products.values('price'))


#
# class Entry(models.Model):
#     item = models.ForeignKey(Item, null=True, on_delete='CASCADE')
#     cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
#     quantity = models.PositiveIntegerField()
#
#     def __str__(self):
#         return "This entry contains {} {}(s).".format(self.quantity,self.item.title)
#
#
# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     line_cost = instance.quantity * instance.item.price
#     instance.cart.total += decimal.Decimal(line_cost)
#     instance.cart.count += instance.quantity
