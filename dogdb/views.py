from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Dog, CallName


class IndexView(generic.ListView):
    model = Dog
    template_name = 'dogdb/index.html'
    context_object_name = 'dogs_list'


class DogView(generic.DetailView):
    model = Dog
    template_name = 'dogdb/dog.html'
    

