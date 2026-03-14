from django.shortcuts import render

# Create your views here.

def product_inventory(request):
    return render(request, 'inventory.html', )

def product_price_list(request):
    return render(request, 'price_list.html')

def product_detail(request):
    return render(request, 'detail.html')

def product_comparator(request):
    return render(request, 'comparator.html')