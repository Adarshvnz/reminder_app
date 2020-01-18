from django.shortcuts import render
from .models import rem
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)
# Create your views here.
class CreateRem(CreateView):
     fields = ("rem_name","rem_on")
     model = rem

     def get_success_url(self):
         return reverse_lazy("rem:remlist")

class ListRem(ListView):
     model = rem

class UpdateRem(UpdateView):
     fields = ("rem_name","rem_on")
     model= rem
     template_name = "rem/update_form.html"

     def get_success_url(self):
         return reverse_lazy("rem:remlist")
