from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import UserRegisterForm
# Create your views here.
class RegisterView(View):

	def get(self,request):
		form = UserRegisterForm()
		return render(request, 'registration/register.html', {'form':form})

	def post(self,request):
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('movie:home')
		else:
			form = UserRegisterForm()
		return render(request, 'registration/register.html', {'form':form})