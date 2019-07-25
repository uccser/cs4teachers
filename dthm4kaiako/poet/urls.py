"""URL routing for POET application."""

from django.urls import path
from poet import views

app_name = 'poet'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('form/', views.FormWizardView.as_view(), name='form'),
]
