from django.urls import path
from .views import index, register_view, store_infomation

urlpatterns = [
    path('', index, name="index"),
    # Hiển thị trang đăng ký
    path('register', register_view, name="register_view"),
    # Hiển thị trang đăng nhập
    path('store-information', store_infomation, name="store-info")
]
