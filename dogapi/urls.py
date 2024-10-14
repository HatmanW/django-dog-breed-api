#dogapi\urls.py
from rest_framework.routers import DefaultRouter
from .views import DogViewSet, BreedViewSet

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)

urlpatterns = router.urls