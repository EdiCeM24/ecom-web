from django.shortcuts import render
from . models import Item



def home(request):
    items = Item.objects.all()
    return render(request, 'port/index.html', {'items': items})


def about(request):
    return render(request, 'port/about.html')


def contact(request):
    return render(request, 'port/contact.html')


def service(request):
    return render(request, 'port/services.html')


def sample(request):
    return render(request, 'port/sample-inner-page.html')


def gallery(request):
    return render(request, 'port/gallery.html')


def gallerySingle(request):
    return render(request, 'port/gallery-single.html')

def nature(request):
    return render(request, 'port/nature.html')
