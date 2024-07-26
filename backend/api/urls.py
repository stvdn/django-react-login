from django.urls import path
from . import views

urlpatterns = [
    path("listall/", views.NoteCreate.as_view(), name="create-note"),
    path("delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note")
]