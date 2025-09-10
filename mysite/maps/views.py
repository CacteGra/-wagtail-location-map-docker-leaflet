# Create your views here.
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'maps/home.html'
    def get_context_data(self, **kwargs):
        from maps.models import Location

        context = super(MainPageView, self).get_context_data(**kwargs)
        context['locations'] = list(Location.objects.values_list('location', flat=True))
        print(context['locations'])
        return context
