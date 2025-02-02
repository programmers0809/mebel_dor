from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    brand = models.CharField(max_length=255, verbose_name='Kim tomonidan')
    # category = models.CharField(max_length=255, verbose_name='Kategoriyasi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    image = models.ImageField(upload_to='products/', verbose_name='Rasmi')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Products'
        managed = True
        verbose_name = 'Mahsulotlar'
        verbose_name_plural = 'Mahsulotlar'
