"""psycho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from .settings import site_name
from blog.models import ArticlePhotoReport
from workers.models import Achievement, Person
from events.models import Event
from shop.models import Product

admin.site.site_header = site_name
admin.site.site_title = site_name
admin.site.index_title = "Добро пожаловать в панель настроек " + site_name

urlpatterns = [
                  path('', RedirectView.as_view(pattern_name='announcement_list'), name='main'),
                  path('blog/', include('blog.urls')),
                  path('', include('main.urls')),
                  path('events/', include('events.urls')),
                  path('workers/', include('workers.urls')),
                  path('mail/', include('mail.urls')),
                  path('shop/', include('shop.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns


ArticlePhotoReport.all_img_from_binary()
Achievement.all_img_from_binary()
Event.all_img_from_binary()
Person.all_img_from_binary()
Product.all_img_from_binary()
