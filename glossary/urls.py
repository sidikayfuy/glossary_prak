from django.urls import path
from . import views

urlpatterns = [
    path('', views.Glossary.as_view(), name="glossary"),
]
