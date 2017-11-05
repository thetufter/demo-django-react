from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ContactForm
from .models import Person
from rest_framework import viewsets, generics
from .serializers import ContactSerializer
import urllib


def home(request):
    contacts = []
    keyword = ""

    # when the search form is submitted
    if request.method == "POST":
        try:
            keyword = request.POST["keyword"]
            contacts = Person.objects.filter(
                Q(name__icontains=keyword) | Q(email__icontains=keyword)
            )[:10]
        except:
            pass

    # the homepage
    else:
        contacts = Person.objects.all().order_by('-id')[:10]

    return render(request, 'homepage.html',
        {'contacts': contacts, 'keyword':keyword})


def new(request):
    # when the 'new contact' form is submitted
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect(home)

    # when the user goes to the 'new contact' page
    else:
        form = ContactForm()

    return render(request, 'new.html', {'form': form})


def react(request):
    return render(request, 'react.html')


class ContactList(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        q = self.request.query_params.get('q', None)
        if q is not None:
            keyword = urllib.parse.unquote(q)
            queryset = queryset.filter(
                Q(name__icontains=keyword) | Q(email__icontains=keyword)
            )
        return queryset
