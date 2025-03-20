from django.db import models

# Create your models here.

class ProductsModel(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", max_length=500)
    photo = models.ImageField("Фото", upload_to="media/%Y/%m/%d", null=True)