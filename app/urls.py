from django.urls import path, include
from .views import NoteDetailView, NoteListView, add_note


urlpatterns = [
    path('notes/', NoteListView.as_view(), name = 'note-list'),
    path('notes/note/<int:pk>/', NoteDetailView.as_view(), name = 'note-detail'),
    path('notes/add/', add_note, name = 'add-note'),
]