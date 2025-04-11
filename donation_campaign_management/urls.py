from django.urls import path, include
from donation_campaign_management import views


urlpatterns = [
    path("<str:id>/donations/", include("donation_management.urls")),
    path("<str:id>/", views.handleDonationCampaignRequest),
    path("", views.createDonationCampaign)
]