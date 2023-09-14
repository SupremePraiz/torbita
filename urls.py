from django.urls import path

from .views import IndexView, ContactView, PortfolioView

urlpatterns = [
    path("",IndexView.as_view(),name="home_page"),
    path("contact",ContactView.as_view(), name="contact_page"),
    path("portfolio/",PortfolioView.as_view(), name="portfolio_page")
]
