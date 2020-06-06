from django.shortcuts import render
from .models import Category, Advert
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy


class AdvertListView(ListView):
    model = Advert
    template_name = 'ad_list.html'


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'ad_detail.html'


class AdvertUpdateView(UpdateView):
    model = Advert
    template_name = 'ad_update.html'


class AdvertDeleteView(DeleteView):
    model = Advert
    template_name = 'ad_delete.html'


class AdvertCreateView(CreateView):
    model = Advert
    template_name = 'ad_create.html'

