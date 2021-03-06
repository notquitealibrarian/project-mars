"""ProjectMars URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from pages import views
from orders.views import CompletedOrders, CurrentOrders, DeniedOrders, OrderFromCatalog, OrderListView, CreateOrderView, OrderDetailView, OrderCopyView, OrderApprove, OrderDeny, SearchOrders, UpdateStatus
from products.views import SearchCatalog
from products import views as prod
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', prod.catalogView, name='catalogue'),
    path('products/<prodID>', prod.prodView, name='product'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/create/', CreateOrderView.as_view(), name='create_order'),
    path('products/<prodID>/order/create/', OrderFromCatalog.as_view(), name='create_order'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<pk>/reorder', OrderCopyView.as_view(), name='reorder'),
    path('orders/<int:pk>/approve', OrderApprove.as_view(), name='order_approve'),
    path('orders/<int:pk>/deny', OrderDeny.as_view(), name='order_deny'),
    path('orders/<int:pk>/update_status', UpdateStatus.as_view(), name='update_status'),
    path('search/', SearchCatalog.as_view(), name='search_catalog'),
    path('orders/current', CurrentOrders.as_view(), name='current_orders'),
    path('orders/completed', CompletedOrders.as_view(), name='completed_orders'),
    path('orders/denied', DeniedOrders.as_view(), name='denied_orders'),
    path('orders/search', SearchOrders.as_view(), name='search_orders'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
