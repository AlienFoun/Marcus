from rest_framework import routers
from .api import UpgradeViewSet

router = routers.DefaultRouter()
router.register('api/upgrade', UpgradeViewSet, 'upgrade')

urlpatterns = router.urls