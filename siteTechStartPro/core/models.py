from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"