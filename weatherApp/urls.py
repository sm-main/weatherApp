"""weatherApp URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^heroku/app/admin/', include(admin.site.urls)),
    url(r'^$','weatherPlot.views.landing_page_view',name='landing_page_view'),
    # url(r'^graph/$','weatherPlot.views.graph_plot_view',name='graph_plot_view'),
    url(r'^ajax/get-points/$','weatherPlot.views.get_points_view',name='get_points_view'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^add/station/$','weatherPlot.views.add_station_view',name='add_station_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register')
]
