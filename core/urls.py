import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("account/", include("account.urls", namespace="account")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("__debug__/", include(debug_toolbar.urls)),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)