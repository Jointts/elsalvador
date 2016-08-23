"""elsalvador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from dbadmin.views import ContEmpresaEditView, ContEmpresaListView, DashboardView, EmpresaListView, EmpresaDetailView, \
    DataClipperListView, EmpresaEditView, DataClipperEditView

urlpatterns = [
    url(r'^empresa/$', EmpresaListView.as_view(), name='empresa.list'),
    url(r'^empresa/(?P<pk>.*)/$', EmpresaDetailView.as_view(), name='empresa.detail'),
    url('r^empresa/edit/(?P<pk>.*)/$', EmpresaEditView.as_view(), name='empresa.edit'),
    url(r'^contEmpresa/$', ContEmpresaListView.as_view(), name='contEmpresa.list'),
    url(r'^contEmpresa/edit/(?P<pk>.*)/$', ContEmpresaEditView.as_view(), name='contEmpresa.edit'),
    url(r'^dataClipper/$', DataClipperListView.as_view(), name='dataClipper.list'),
    url(r'^dataclipper/edit/(?P<pk>.*)/$', DataClipperEditView.as_view(), name='dataClipper.edit'),
    url(r'^$', DashboardView.as_view(), name='dashboard')
]


