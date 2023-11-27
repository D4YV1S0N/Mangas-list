from django.db import models

# Create your models here.
class Mangas(models.Model):
  manga_name = models.CharField(max_length=50)
  manga_cap = models.CharField(max_length=5)
  manga_status = models.CharField(max_length=10)
  
  def __str__(self):
    return self.manga_name