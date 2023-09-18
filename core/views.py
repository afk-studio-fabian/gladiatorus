from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {"page_title":"Bruker"}
    return render(request, "pages/welcome.html", context)