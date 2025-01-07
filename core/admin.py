from django.contrib import admin

from core.models import Agency, Astronaut, Planet, Mission, Spacecraft

# Register your models here.
admin.site.register(Agency)
admin.site.register(Astronaut)
admin.site.register(Planet)
admin.site.register(Mission)
admin.site.register(Spacecraft)

