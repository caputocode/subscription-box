from django.db import models

# Create your models here.

class Offer(models.Model):
    """
    Model for Subscription Service Ad
    """
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    votes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True) 
    
    
    def __str__(self):
        """
        Returns a String with title of subscription offer
        """
        return self.title