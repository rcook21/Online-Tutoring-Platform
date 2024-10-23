from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(success)
  else:
    form = UserForm()
  return render(request, 'login.html', {'form': form})

def success(request):
  return render(request, 'homepage.html')
