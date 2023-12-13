from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {"page_title":"Welcome"}
    return render(request, "pages/welcome.html", context)


def home(request):
    context = {"page_title":"Welcome"}
    return render(request, "pages/welcome.html", context)


# ############################################
#
# - Core menu Parts
#

def gmm_core_view(request):
    context = {}
    
    #if user isn't logged in
    gmm_core_path = "components/core/gmm-core/gmm-core-template.html"

    #if logged in
    if request.user.is_authenticated:
        gmm_core_path = request.user.userorientation.get_template()

    return render(request, gmm_core_path, context)

