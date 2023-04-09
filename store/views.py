from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.views.generic import DetailView
from django.utils.text import slugify
from django.urls import reverse
import stripe
from django.conf import settings




# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'store/index.html',{
        'products':products,
    })

def contact(request):
    return render(request,'store/contact.html')

def about(request):
    return render(request,'store/about.html')

class ProductDetailView(DetailView):
    model=Product
    slug_url_kwarg='name'
    slug_field='name'

    queryset=Product.objects.filter()
def cart(request):
    return render(request,'store/cart.html')


def order(request):
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=OrderForm

    return render(request,'store/order.html',{
        'form':form,
    })

def ship(request):
    if request.method == "POST":
        form=AddressForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return reverse('payment')

    else:
            form=AddressForm
    
    return render(request,'store/address.html',{'form':form})

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Example charge',
            source=token
        )
        return render(request, 'store/payment.html')
    return render(request, 'store/payment.html')



