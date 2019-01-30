from django.shortcuts import render

# Create your views here.
def index(request):
    """
    View containing Index Home Page 
    """
    return render(request, 'index.html')