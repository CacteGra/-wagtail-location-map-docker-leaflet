from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel
from wagtailgeowidget.panels import LeafletPanel

from .models import Location

class LocationTemplate(SnippetViewSet):
    model = Location

    panels = [
        # Here is defined which fields are displayed
       	# and what panel type is used to display them
        FieldPanel("location_name"),
        LeafletPanel("location"),
    ]

register_snippet(LocationTemplate)
