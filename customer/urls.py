from django.urls import path
from .views import index, login_process, login_view, logout, register_view, store_infomation, add_to_cart, payment_view, store_payment_information

urlpatterns = [
    path('', index, name="index"),
    # Hiển thị trang đăng ký
    path('register', register_view, name="register_view"),
    # Lưu thông tin khách hàng đăng ký
    path('store-information', store_infomation, name="store_info"),
    # Hiển thị trang đăng nhập
    path('login', login_view, name="login_view"),
    # Kiểm tra đăng đăng
    path('login-process', login_process, name="login_process"),
    # Đăng xuất
    path('logout', logout, name="logout"),
    path('add-to-cart/<int:id>/', add_to_cart, name="add_to_cart"),
    path('payment', payment_view, name="payment"),
    path('store-payment-information', store_payment_information,
         name="store-payment-information"),
]
