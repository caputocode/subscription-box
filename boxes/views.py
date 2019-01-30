from django.shortcuts import render, HttpResponse
from .models import Box


def display_boxes(request):
    """
    View to show all box subscriptions available
    """
    boxes = Box.objects.all()
    return render(request, 'boxes.html', {'boxes': boxes} )
