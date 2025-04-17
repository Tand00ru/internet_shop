from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^cart/', include("cart.urls")),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    re_path(r'^admin_panel/', include('admin_panel.urls')),
    re_path(r'^', include('shop.urls', namespace='shop')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
