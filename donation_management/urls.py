from django.urls import path
from donation_management import views

urlpatterns = [
    path("", views.addDonation)
]