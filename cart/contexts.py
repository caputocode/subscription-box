from django.shortcuts import get_object_or_404
from boxes.models import Box

def cart_contents(request):
    """
    Ensures that cart contents are availiable when
    rendering every page within app
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Box, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'product': product})
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}