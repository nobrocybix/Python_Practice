from django.db import models

# Create your models here.
class Pizza(models.Model):
    '''A pizza model for storing the pizza's name.'''
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    '''A topping model is used to store pizza toppings.'''
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    
    def __str__(self):
        if len(self.topping_name) < 50:
            return self.topping_name[:50]
        else:
            return self.topping_name[:50] + "..."