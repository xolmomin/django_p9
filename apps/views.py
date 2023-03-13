from django.shortcuts import render
from apps.forms import ContactForm


def index_page(request):
    context = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
    return render(request, 'index.html', context)


def menu_page(request):
    return render(request, 'menu.html')
