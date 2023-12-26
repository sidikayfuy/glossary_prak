from django.urls import path
from . import views

urlpatterns = [
    path('', views.GlossaryView.as_view(), name="glossary"),
]
