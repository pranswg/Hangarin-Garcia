from django.apps import AppConfig
from django.views.generic import TemplateView


class HangarinprojConfig(AppConfig):
    name = 'hangarinproj'

class HomePageView(TemplateView):
    template_name = "home.html"

class AircraftListView(TemplateView):
    template_name = "aircraft_list.html"

class AircraftCreateView(TemplateView):
    template_name = "aircraft_form.html"
