from django.shortcuts import render

# Create your views here.
def concept(request):
    """
    View containing About Us Page 
    """
    return render(request, 'concept.html')