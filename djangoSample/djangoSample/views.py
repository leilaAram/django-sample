from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


# def home_page(request):
#     return HttpResponse("<h1>Hello World</h1>")
def home_page(request):
    my_title = " Hello there ... "
    return render(request, "hello_world.html", {"title": my_title})

def about_page(request):
    return render(request, "hello_world.html", {"title": "About Us"})

def cuntact_page(request):
    return render(request, "hello_world.html", {"title": "Cuntact Us"})

def example_page(request):
    context = {"title":"Example Page"}
    templat_name = "hello_world.html"
    templat_object = get_template(templat_name)
    return HttpResponse(templat_object.render(context))