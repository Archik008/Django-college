from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField("Имя", max_length=200)
    description = models.TextField("Описание")
    photo = models.ImageField("Фотография", upload_to="photos/%Y/%m/%d")

    def __str__(self):
        return self.name