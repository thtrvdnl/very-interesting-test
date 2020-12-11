from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'core/base.html')

@login_required
def home(request):
    return render(request, 'core/home.html')