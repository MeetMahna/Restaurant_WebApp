from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import FoodForm
from .models import Food, Item
from django.contrib.auth.models import User

# Create your views here.


def homepage(response):

    return render(response, 'home/homepage.html')


def menu(response):
    if response.user.is_active:
        food_data = Food.objects.all()

        '''if response.method == 'POST':
            form = FoodForm(response.POST)
            if form.is_valid():
            form = FoodForm()'''

        print(food_data)
        return render(response, 'home/menu.html',{'food_data': food_data})
    else:
        return HttpResponseRedirect("/login")


def category(response, id, qty):
    if response.user.is_active:
        print('hello')
        item_data = Item.objects.get(id=id)
        item_data.item_qty = qty
        print(item_data,':',item_data.item_price,':',item_data.item_qty)
        item_data.save()

        return redirect("menu")
    else:
        return HttpResponseRedirect("/login")


def checkout(response):
    if response.user.is_active:
        item_data = Item.objects.all()
        total = 0
        for item in item_data:
            total = total + item.item_price * item.item_qty

        return render(response, 'home/checkout.html',{'total':total, 'item_data': item_data})
    else:
        return HttpResponseRedirect("/login")


def delete_item(response, id):
    item_data = Item.objects.get(id=id)
    item_data.item_qty = 0
    print(item_data,':',item_data.item_price,':',item_data.item_qty)
    item_data.save()

    return redirect("checkout")


def clear_cart(response):
    item_data = Item.objects.all()
    for item in item_data:
        item.item_qty = 0
        item.save()

    return redirect("checkout")


def summary(response):
    item_data = Item.objects.all()
    total = 0
    for item in item_data:
        total = total + item.item_price * item.item_qty

    return render(response, 'home/summary.html', {'total': total, 'item_data': item_data})
