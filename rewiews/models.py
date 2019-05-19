from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    purchase = models.ForeignKey(to='game.Game', related_name='customers', on_delete=models.CASCADE,)

class Review(models.Model):
    customer = models.ForeignKey(to='rewiews.Customer', related_name='reviews', on_delete=models.CASCADE,)
    description = models.TextField(max_length=1000)
    game = models.ForeignKey(to='game.Game', related_name='reviews', on_delete=models.CASCADE,)
