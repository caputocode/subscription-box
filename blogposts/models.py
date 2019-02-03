from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    Model for a single post
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True) 
    
    
    def __str__(self):
        """
        Returns a String with title of post
        """
        return self.title