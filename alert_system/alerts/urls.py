from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, DashboardViewSet

router = DefaultRouter()

router.register(r'alerts', AlertViewSet)
router.register(r'dashboard', DashboardViewSet, basename='dashboard')

urlpatterns = router.urls