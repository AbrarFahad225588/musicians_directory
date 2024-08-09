from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'music/musician_list.html', {'musicians': musicians})
def all_musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'music/all_musician.html', {'musicians': musicians})

def create_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'music/musician_form.html', {'form': form})

def edit_musician(request, id):
    musician = get_object_or_404(Musician, id=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('all_musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'music/musician_form.html', {'form': form})

def delete_musician(request, id):
    musician = get_object_or_404(Musician, id=id)
    musician.delete()
    return redirect('all_musician_list')

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'music/album_form.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_form.html', {'form': form})

def delete_album(request, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return redirect('musician_list')
