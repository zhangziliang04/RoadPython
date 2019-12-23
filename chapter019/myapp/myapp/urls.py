"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf.urls import url
from . import view
from . import search
from . import dbhandler


urlpatterns = [
    url(r'^$', view.hello2),
    url(r'^hello1$', view.hello1),
    url(r'^hello2$', view.hello2),
    url(r'^add$', dbhandler.add_db),
    url(r'^query$', dbhandler.query_db),
    url(r'^edit$', dbhandler.update_db),
    url(r'^del$', dbhandler.del_db),
    #
    url(r'^login$', search.login),
    url(r'^login_form$', search.login_form),

]
