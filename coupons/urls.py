from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('', views.coupon_apply, name='coupon_apply'),
    path('remove/', views.coupon_remove, name='coupon_remove'),
]