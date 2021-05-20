from django.urls import path
from .views import index, register_view

urlpatterns = [
    path('', index, name="index"),
    # Hiển thị trang đăng ký
    path('register', register_view, name="register_view"),
    # Hiển thị trang đăng nhập
]
