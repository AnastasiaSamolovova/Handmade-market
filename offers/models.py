from django.db import models
from products.models import Product, Color
from django.template.defaultfilters import slugify


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    slug = models.SlugField(max_length=160, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.product.name}_{self.color.name}")
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        return f"Offer {self.id} {self.slug} [{self.price} ₽]"
