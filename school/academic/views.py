from django.views.generic import ListView
from .models import Session, Version

class SessionListView(ListView):
    model = Session
    template_name = 'session_list.html'  # Ensure this template exists
    context_object_name = 'sessions'

class VersionListView(ListView):
    model = Version
    template_name = 'version_list.html'  # Ensure this template exists
    context_object_name = 'versions'