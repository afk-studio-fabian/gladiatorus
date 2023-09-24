from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {"page_title":"Welcome"}
    return render(request, "pages/welcome.html", context)


def home(request):
    context = {"page_title":"Welcome"}
    return render(request, "pages/welcome.html", context)