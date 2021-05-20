from django.shortcuts import render
from .models import Category


def index(request):
    # ORM của DJANGO
    # Lấy tất cả dữ liệu của 1 bảng: Objects.all()
    category = Category.objects.all()

    # dữ liệu được đưa vào phải là dictionary {}
    return render(request, "customer/index.html", {"category": category})


def register_view(request):
    return render(request, "customer/register.html")
