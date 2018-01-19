from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            "name": "Leigh",
            "names": ["Gunter", "Glieben", "Glauten", "Globen"]
        }
        return render(request, 'index.html', context=context)


class AboutPageView(TemplateView):
    template_name = "about.html"
