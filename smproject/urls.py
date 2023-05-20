"""smproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from smapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('addProductForm',views.AddProduct,name='addProduct'),
    path('productTable',views.ShowProduct,name='productTable'),
    path('LogIn',views.view_login,name='LogIn'),
    path('logout',views.logout_view,name='logout'),
    path('delete/<int:id>',views.delete_row,name='delete'),
    path('showProductRow/<int:id>',views.show_product_row,name='showProductRow'),
    path('showProductRow/editProductRow/<int:id>',views.edit_product_row,name='editProductRow'),
    path('retailerTable',views.retailer_table,name='retailerTable'),
    path('buyProduct/<int:id>',views.buy_product,name='buyProduct'),
    path('supplierpage',views.supplier_page,name='supplierpage'),
    path('retailerpage',views.retailer_page,name='retailerpage'),
    path('purchaseHistory',views.purchase_history,name='purchaseHistory'),
    path('retailerHistory',views.retailer_history,name='retailerHistory'),
]
#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)