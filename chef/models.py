from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class MenuModel(models.Model):
    food_name = models.CharField(max_length=100)
    food_pic = models.ImageField(
        default="default.png", null=True, blank=True)
    food_cat = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=6, decimal_places=0)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        url_slug = {'slug': self.slug}
        return reverse('chef:listmakanan', kwargs=url_slug)

    def __str__(self):
        return "{}.{}".format(self.id, self.food_name)
