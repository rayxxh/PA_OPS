# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView
# from django.contrib import messages


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


    
class BootstrapView(TemplateView):
    template_name = 'account/login.html'

class IndexView(TemplateView):
    template_name = 'dashboard/index.html'

class BlankView(TemplateView):
    template_name = 'PA_OPS/blank.html'
   
class ButtonsView(TemplateView):
    template_name = 'PA_OPS/buttons.html'

class FlotView(TemplateView):
    template_name = 'PA_OPS/flot.html'

class FormsView(TemplateView):
    template_name = 'PA_OPS/forms.html'

class GridView(TemplateView):
    template_name = 'PA_OPS/grid.html'
class IconsView(TemplateView):
    template_name = 'PA_OPS/icons.html'
class LoginView(TemplateView):
    template_name = 'PA_OPS/login.html'
class MorrisView(TemplateView):
    template_name = 'PA_OPS/morris.html'
class NotificationsView(TemplateView):
    template_name = 'PA_OPS/notifications.html'
class PanelsWellsView(TemplateView):
    template_name = 'PA_OPS/panels-wells.html'
class TablesView(TemplateView):
    template_name = 'PA_OPS/tables.html'
class TypographView(TemplateView):
    template_name = 'PA_OPS/typography.html'
