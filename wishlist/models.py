from pyexpat import model
from django.db import models

# Create your models here.

class BarangWishList(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi =  models.TextField()