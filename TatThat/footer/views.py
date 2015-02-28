from django.views.generic import TemplateView

class FooterAboutView(TemplateView):
    template_name = 'footer_about.html'

class FooterTermView(TemplateView):
    template_name = 'footer_term.html'

class FooterPrivacyView(TemplateView):
    template_name = 'footer_privacy.html'