from django.shortcuts import render, get_object_or_404
from .models import Mangas

# Create your views here.

def index(request):
  manga_name = Mangas.objects.all()
  return render(request, "mangman/index.html", {"manga_name": manga_name})