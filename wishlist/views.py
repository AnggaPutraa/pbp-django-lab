from multiprocessing import context
from django.shortcuts import render
from wishlist.models import BarangWishList

wishlist_data_barang = BarangWishList.objects.all()
context = {
    'list_barang' : wishlist_data_barang,
    'nama' : 'Kak Cinoy'
}

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)