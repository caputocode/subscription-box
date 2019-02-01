from django.shortcuts import render, get_object_or_404
from .models import Box


def display_boxes(request):
    """
    View to show all box subscriptions available
    """
    boxes = Box.objects.all().order_by('price')
    return render(request, 'boxes.html', {'boxes': boxes} )
 
def box_detail(request, pk):
    """
    Create a view that returns a single post object
    based on the post ID (pk) and render it to the
    'postdetail.html' template. Or return a 404 error
    if the post is not found
    """
    box = get_object_or_404(Post, pk=pk)
    box.views += 1
    box.save()
    return render(request, 'display-boxes.html', {'box': box })