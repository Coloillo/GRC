from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskViewSet
from .api_views import ApiRiskViewSet, ApiRiskTreatmentViewSet

router = DefaultRouter()
router.register(r'legacy-risks', RiskViewSet, basename='risk')
router.register(r'risks', ApiRiskViewSet, basename='api-risk')

# API Routes
urlpatterns = [
    path('', include(router.urls)),
    
    # API Risk metrics endpoint
    path('risks/metrics/', ApiRiskViewSet.as_view({'get': 'metrics'})),
    
    # API Risk Treatment routes
    path('risks/<int:risk_pk>/treatments/', ApiRiskTreatmentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('risks/<int:risk_pk>/treatments/<int:pk>/', ApiRiskTreatmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
] 