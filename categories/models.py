from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True)
    cat_img = models.ImageField(upload_to='static/img/', blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'