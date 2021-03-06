

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("about/", views.about, name = "AboutUs"),
    path("contact", views.contact, name = "ContactUs"),
    path("search", views.search, name = "Search"),
    path("productview", views.prodView, name = "Product"),
    path("tracker", views.track, name = "Tracking")
    

]
