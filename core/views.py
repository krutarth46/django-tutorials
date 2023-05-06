from django.views import generic


class HomeView(generic.TemplateView):
    """
        Website homepage view

        ** template: **

        :template: `core/index.html`
    """
    template_name = "core/index.html"
