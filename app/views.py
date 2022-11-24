from django.shortcuts import render

# Create your views here.
def jinja_tags(request):
    return render(request,'jinja_tags.html')