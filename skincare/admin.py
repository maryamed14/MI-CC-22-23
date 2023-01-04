from django.contrib import admin

# Register your models here.
from .models import Issue
from .models import Person

admin.site.register(Issue)
admin.site.register(Person)
