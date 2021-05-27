from django.shortcuts import redirect, render
from .models import Category, Customer, Order, Order_Detail, Product
import hashlib
from django.urls import reverse


def index(request):
    if 'customer' in request.session:
        email_customer = request.session['customer']
        # ORM của DJANGO
        # Lấy tất cả dữ liệu của 1 bảng: Objects.all()
        category = Category.objects.all()
        product = Product.objects.all()
        # customer = Customer.objects.get(email=email_customer)
        # order = Order.objects.filter(is_ordered=False, customer=customer)
        # order_details = Order_Detail.objects.complex_filter(order=order)
        # print(order_details)

        context = {
            "category": category,
            "product": product,
            "customer": email_customer
        }
        # dữ liệu được đưa vào phải là dictionary {}
        return render(request, "customer/index.html", context)

    return redirect('login_view')


def register_view(request):
    if 'customer' in request.session:
        return redirect('index')

    return render(request, "customer/register.html")


def store_infomation(request):
    # object
    customer = Customer()  # instance
    customer.first_name = request.POST.get('first-name')
    customer.last_name = request.POST.get('last-name')
    customer.email = request.POST.get('email')
    password = request.POST.get('password')
    customer.password = hashlib.md5(password.encode()).hexdigest()
    customer.save()  # store data to database
    return redirect('index')


def login_view(request):
    if 'customer' in request.session:
        return redirect('index')

    context = {}
    if request.GET.get('error'):
        context = {'error': 'Wrong email or password'}
    return render(request, "customer/login.html", context)


def login_process(request):
    if request.method == "POST":
        # Nhận dữ liệu đã post
        email = request.POST.get('email')
        password = request.POST.get('password')
        # mã hoá md5 với pass đó
        pass_hash_md5 = hashlib.md5(password.encode()).hexdigest()
        customer_check = Customer.objects.filter(
            email=email, password=pass_hash_md5)
        if customer_check:
            request.session["customer"] = email
            return redirect('index')
        url = f"{reverse('login_view')}?error=true"
        return redirect(url)
    else:
        return redirect('login_view')


def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('login_view')
    return redirect('login_view')


def add_to_cart(request, id):
    if 'customer' in request.session:
        email = request.session['customer']
        # Đi tìm sản phẩm
        product = Product.objects.get(id=id)
        order = Order.objects.last()
        order_detail = Order_Detail.objects.filter(
            order=order, product=product)
        if order == None:
            customer = Customer.objects.get(email=email)
            order = Order()
            order.customer = customer
            order.save()

        if order_detail:
            quantity = order_detail.first().quantity + 1
            order_detail.update(quantity=quantity)
        else:
            order_detail = Order_Detail()
            order_detail.order = order
            order_detail.product = product
            order_detail.price = product.price
            order_detail.quantity = 1
            order_detail.save()

    return redirect('index')
