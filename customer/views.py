from django.shortcuts import redirect, render
from .models import Category, Customer, Product
import hashlib


def index(request):
    # ORM của DJANGO
    # Lấy tất cả dữ liệu của 1 bảng: Objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        "category": category,
        "product": product
    }
    # dữ liệu được đưa vào phải là dictionary {}
    return render(request, "customer/index.html", context)


def register_view(request):
    return render(request, "customer/register.html")


def store_infomation(request):
    # object
    customer = Customer()  # instance
    customer.first_name = request.POST.get('first-name')
    customer.last_name = request.POST.get('last-name')
    customer.email = request.POST.get('email')
    password = request.POST.get('password')
    customer.password = hashlib.md5(password.encode())
    customer.save()  # store data to database
    return redirect('index')
