from django.db import models

# Create your models here.

class Box(models.Model):
    """
    Model for each Box
    """
    
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=500, default='')
    contents = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        """
        Returns a String with name of box
        """
        return self.name