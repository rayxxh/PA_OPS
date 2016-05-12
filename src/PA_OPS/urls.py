"""PA_OPS URL Configuration

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
from django.conf.urls import patterns, url
from django.contrib import admin
from PA_OPS.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BootstrapView.as_view() ),
    url(r'^index$',IndexView.as_view(),name='index' ),
    url(r'^blank$', BlankView.as_view(), name='blank' ),
    url(r'^buttons', ButtonsView.as_view() , name='buttons'),
    url(r'^flot', FlotView.as_view(), name='flot'),
    url(r'^forms$', FormsView.as_view(), name='form' ),
    url(r'^grid$', GridView.as_view() , name='grid'),
    url(r'^icons$', IconsView.as_view() , name='icon'),
    url(r'^login$', LoginView.as_view() , name='login'),
    url(r'^morris$', MorrisView.as_view(), name='morris' ),
    url(r'^notifications$', NotificationsView.as_view(), name='notifications' ),
    url(r'^panels-wells$', PanelsWellsView.as_view() , name='panels-wells'),
    url(r'^tables$', TablesView.as_view() , name='tables'),
    url(r'^typography$', TypographView.as_view() , name='typography'),
    
]
# urlpatterns = patterns('',
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', BootstrapView, name='BootstrapView'), 
# )
