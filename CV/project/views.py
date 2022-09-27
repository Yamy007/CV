from django.shortcuts import render

# Create your views here.
def project(request):
    return render(request, "pages/project.html") #this page must have all content about project