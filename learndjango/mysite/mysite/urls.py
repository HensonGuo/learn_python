"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from learn import views as learn_views
from blog import views as blog_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('users.urls')),
    url(r'^$', learn_views.home, name='home'),
    url(r'^add/', learn_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^test/', learn_views.test, name='test'),
    url(r'^test_render_2_response/', learn_views.test_render_2_response, name='test'),
    url(r'^model_test/', learn_views.model_test, name='model_test'),
    url(r'^field_test/', learn_views.field_test, name='field_test'),
    url(r'^form_test/', blog_views.index, name='form_test'),
]
