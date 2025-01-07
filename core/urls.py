from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import AgencyViewSet, AstronautViewSet, PlanetViewSet, MissionViewSet, SpacecraftViewSet

router = DefaultRouter()
router.register(r'agencies', AgencyViewSet)
router.register(r'astronauts', AstronautViewSet)
router.register(r'planets', PlanetViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'spacecrafts', SpacecraftViewSet)

urlpatterns = router.urls