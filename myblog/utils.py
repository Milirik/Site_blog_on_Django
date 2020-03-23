from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListMixin():
	model = None
	template = None

	def get(self, request):
		model_list = self.model.objects.all()
		return render(request,
					  self.template,
					  context={self.model.__name__.lower()+'s_list':model_list})


class DetailMixin():
	model = None
	template = None

	def get(self, request, slug):
		model_ = get_object_or_404(self.model, slug__iexact=slug)
		return render(request,
					  self.template,
					  context={self.model.__name__.lower():model_})
