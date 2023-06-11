from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "frogs_by_sam/home.html"

