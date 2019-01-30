from django.test import TestCase
from .models import Box

# Create your tests here.
class BoxTest(TestCase):
    """
    Define tests that will run against Box models
    """
    
    def test_str(self):
        test_name = Box(name='A subscription box')
        self. assertEqual(str(test_name), 'A subscription box')