# urls.py

from django.urls import path
from .views import (
    ServicesListView,
    ProjectListView,
    TestimonialListView,
    OurClientsListView,OurTeamListView,
    contact_view,
    submit_quote
)

urlpatterns = [
    path('api/services/', ServicesListView.as_view(), name='services-list'),
    path('api/projects/', ProjectListView.as_view(), name='projects-list'),
    path('api/testimonials/', TestimonialListView.as_view(), name='testimonials-list'),
    path('api/clients/', OurClientsListView.as_view(), name='clients-list'),
    path('api/team/', OurTeamListView.as_view(), name='team-list'),
    path('api/contact/', contact_view, name='contact'),
    path('api/submit-quote/', submit_quote, name='contact'),
]
