from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Shop


def home(request):
	return render(request,'home.html')


class ShopCreate(CreateView):
	model = Shop
	fields = "__all__"
	template_name = 'first/shop_create.html'
	success_url = reverse_lazy('home')

class ShopUpdate(UpdateView):
	model = Shop
	fields = "__all__"
	template_name = 'first/shop_update.html'
	success_url = "/"

class ShopDelete(DeleteView):
	model = Shop
#	fields = "__all__"
	template_name = 'first/shop_delete.html'
	success_url = '/'

class ShopList(ListView):
	model = Shop
	template_name = 'first/shop_list.html'


class ShopDetail(DetailView):
	model = Shop
	template_name = 'first/shop_detail.html'




