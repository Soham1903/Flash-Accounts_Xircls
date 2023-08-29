from django.shortcuts import render, redirect, HttpResponse
from .models import *
import json
from django.http import JsonResponse
from .models import toggle
from django.views.decorators.csrf import csrf_exempt
from .models import *
import requests
from .test import *
from .serializers import *;


shop = "sohamladgaonkar.myshopify.com"
@csrf_exempt
def index(request):
    shop = toggle.objects.first()  

    if not shop:
        shop = toggle.objects.create(shopname="sohamladgaonkar.myshopify.com", toggle_value=False)

    if request.method == "POST":
        toggle_value = request.POST.get("toggleSwitch")
        print(toggle_value)
        shop.toggle_value = True if toggle_value == "on" else False
        shop.save()
        data = {'message':'working'}
        return JsonResponse(data)
    elif request.method == "GET":
        return render(request, 'index.html')    
 
@csrf_exempt
def valuetog(request):
    if request.method == 'POST':
        shopname = request.POST.get('shop')
        obj = toggle.objects.get(shopname= shopname)
        value = obj.toggle_value
    return JsonResponse({'value': value})

#Total Customers Present
@csrf_exempt
def cust_count(request):
    url = "https://sohamladg.myshopify.com/admin/api/2023-07/customers/count.json"

    payload = {}
    headers = {
        'X-Shopify-Access-Token': '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',
        'Cookie': '_shopify_y=78daa286-0670-4f9e-a090-e0786c014af6; _y=78daa286-0670-4f9e-a090-e0786c014af6; localization=IN; secure_customer_sig='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()  # Parse the JSON response

    serializer = CountSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return JsonResponse(serializer.validated_data, safe=False)

# Customers registered through our form
@csrf_exempt
def button_click_view(request):
    if request.method == 'POST':
        print("hellodwd")
        shopname = "sohamladg.myshopify.com/"
        try:
            shop = Shop.objects.get(shopname=shopname)
            shop.count += 1
            shop.save()
        except Shop.DoesNotExist:
            shop = Shop.objects.create(shopname=shopname, count=1)
        
        # Return the shopname and count in the JSON response
        response_data = {
            'success': True,
            'shopname': shop.shopname,
            'count': shop.count,
        }
        return JsonResponse(response_data)
    
    # If the request method is not POST
    return JsonResponse({'success': False})