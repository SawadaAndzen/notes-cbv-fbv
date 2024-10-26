from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('note-list')
    else:
        form = NoteForm()
        
    return render(request, 'add_note.html', {'form': form})