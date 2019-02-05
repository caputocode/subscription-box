from django.shortcuts import render
from .models import Offer
# Create your views here.

def display_offers(request):
    """
    View to show all Subscription Offers available 
    """
    offers = Offer.objects.all().order_by('price')
    return render(request, 'offers.html', {'offers': offers })
