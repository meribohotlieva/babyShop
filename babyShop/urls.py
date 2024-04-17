"""
URL configuration for babyShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .accounts.views import ProfileView
from .products.views import HomeView
from .products import views
from .accounts import views as accounts_views
from .cart import views as cart_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('products/', views.products_list, name='product_list'),
    path('register/', accounts_views.register, name='register'),
    path('cart/', cart_views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]