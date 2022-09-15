from django.shortcuts import render
from wishlist.models import BarangWishList
from django.http import HttpResponse
from django.core import serializers

def show_wishlist(request):
    data = BarangWishList.objects.all()

    return render(
        request, 
        "wishlist.html", 
        {
            'list_barang' : data,
            'nama' : 'Angga'
        }
    )

def show_wishlist_xml(request):
    data = BarangWishList.objects.all()

    return HttpResponse(
        serializers.serialize("xml", data), 
        content_type="application/xml"
    )

def show_wishlist_json(request):
    data = BarangWishList.objects.all()

    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )

def show_json_by_id(request, id):
    data = BarangWishList.objects.filter(pk = id)

    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )

def show_xml_by_id(request, id):
    data = BarangWishList.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize("xml", data), 
        content_type="application/xml"
    )
