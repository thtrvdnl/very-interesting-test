from .models import Place
from .utils import add_map
from .form import PlaceForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def base(request):
    return render(request, 'core/base.html')


@login_required(redirect_field_name='')
def home(request):
    places = Place.objects.filter(user=request.user)
    return render(request, 'core/home.html', {'places': places})


@login_required(redirect_field_name='')
def add_note(request):
    error = ''
    username = get_object_or_404(User, id=request.user.id)

    map = add_map()

    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = username
            note.save()
            return redirect('home')
        else:
            error = "Форма введена неверно"

    form = PlaceForm()
    context = {
        'map': map,
        'form': form,
        'error': error
    }
    return render(request, 'core/create.html', context)
