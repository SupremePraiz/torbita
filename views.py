from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from django.views.generic.edit import DeleteView

from .models import Registration
from .forms import RegistrationForm
# Create your views here.

class IndexView(TemplateView):
    template_name = "account/home.html"


class ContactView(CreateView):
    template_name = "account/contact.html"
    model = Registration
    form_class = RegistrationForm
    success_url = "/portfolio/"
    success_message = "profile updated successfully"
    

    
class PortfolioView(TemplateView):
    template_name = "account/portfolio.html"
