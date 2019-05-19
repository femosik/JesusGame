from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(to='categories.Category', related_name='games', on_delete=models.CASCADE, )
    img = models.CharField(max_length=150)
