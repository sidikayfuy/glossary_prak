from django.contrib import admin
from .models import Term

for i in [Term]:
    admin.site.register(i)
