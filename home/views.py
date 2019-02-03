from django.shortcuts import render

# Create your views here.
def concept(request):
    """
    View containing About Us Page 
    """
    return render(request, 'concept.html')
    
def following(request):
    """
    View containing Social Media Following Page 
    """
    return render(request, 'following.html')