
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index,name="home"),
    path("contact", views.contact,name="contact"),
    path("message", views.message,name="message"),
    path("about", views.about,name="about"),
    path("search", views.search, name="search"),
    path("car/<int:carID>", views.carDisplay, name="car")
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
