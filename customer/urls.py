from django.urls import path
from .views import index, login_process, login_view, logout, register_view, store_infomation

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
]
