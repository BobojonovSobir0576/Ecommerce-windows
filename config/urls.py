
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
admin.site.site_url = None

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="doc.html", extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),

    path('auth/api/', include('authentification.urls')),
    path('admin-panel/api/', include('admin_panel.urls')),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]