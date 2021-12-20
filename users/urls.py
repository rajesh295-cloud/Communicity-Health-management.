from django import urls
from . import views
urlspattern = [
    path('home', views.home )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)