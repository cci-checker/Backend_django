"""checker URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from data_api import views as api_views
from display import views as display_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', api_views.userlist.as_view()),
    url(r'^checklist/', api_views.checklist_list.as_view()),
    url(r'^room/', api_views.rooms.as_view()),
    url(r'^checkoff_list/', api_views.checkofflist.as_view()),
    #url(r'^list_items/', views.listitems.as_view()),
    url(r'^issuereport/', api_views.Issuereport.as_view()),
    url(r'^display/', display_views.displayfunction, name='dispayscreen')



]
urlpatterns = format_suffix_patterns(urlpatterns)
# change this, when turning off debug
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


