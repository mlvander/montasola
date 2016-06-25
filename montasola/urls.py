"""montasola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

from django.conf.urls.static import static
from montasola import settings
from imageManager.views import initialDatabaseSetup, imageGalleries, imageGallery
from montasola.views import homePage

urlpatterns = [
    url(r'^$', homePage.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^gallery/$', imageGalleries.as_view()),
    url(r'^gallery/([0-9]{1,4})/$', imageGallery.as_view()),
    url(r'^initialDatabaseSetup/$', initialDatabaseSetup.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
