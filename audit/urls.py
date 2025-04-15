from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApiAuditViewSet, ApiControlViewSet, ApiFindingViewSet

router = DefaultRouter()
router.register(r'audits', ApiAuditViewSet, basename='api-audit')
router.register(r'controls', ApiControlViewSet, basename='api-control')
router.register(r'findings', ApiFindingViewSet, basename='api-finding')

urlpatterns = [
    path('', include(router.urls)),
] 