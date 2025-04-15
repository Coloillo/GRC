from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ApiRisk, ApiRiskTreatment
from .serializers import ApiRiskSerializer, ApiRiskTreatmentSerializer

class ApiRiskViewSet(viewsets.ViewSet):
    """
    ViewSet for ApiRisk model
    """
    def list(self, request):
        risks = ApiRisk.objects.all()
        serializer = ApiRiskSerializer(risks, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=pk)
            serializer = ApiRiskSerializer(risk)
            return Response(serializer.data)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        serializer = ApiRiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=pk)
            serializer = ApiRiskSerializer(risk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=pk)
            risk.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def metrics(self, request):
        # Get severity counts
        critical_count = ApiRisk.objects.filter(severity='critical').count()
        high_count = ApiRisk.objects.filter(severity='high').count()
        medium_count = ApiRisk.objects.filter(severity='medium').count()
        low_count = ApiRisk.objects.filter(severity='low').count()
        
        # Get status counts
        open_count = ApiRisk.objects.filter(status='open').count()
        mitigated_count = ApiRisk.objects.filter(status='mitigated').count()
        accepted_count = ApiRisk.objects.filter(status='accepted').count()
        transferred_count = ApiRisk.objects.filter(status='transferred').count()
        closed_count = ApiRisk.objects.filter(status='closed').count()
        
        # Get total count
        total_count = ApiRisk.objects.count()
        
        # Get recent risks (limit to 3)
        recent_risks = ApiRisk.objects.all().order_by('-created_at')[:3]
        recent_risks_data = [
            {
                'id': risk.id,
                'title': risk.title,
                'severity': risk.severity
            }
            for risk in recent_risks
        ]
        
        return Response({
            'critical': critical_count,
            'high': high_count,
            'medium': medium_count,
            'low': low_count,
            'total': total_count,
            'open_risks': open_count,
            'closed_risks': closed_count,
            'status_counts': {
                'open': open_count,
                'mitigated': mitigated_count,
                'accepted': accepted_count,
                'transferred': transferred_count,
                'closed': closed_count
            },
            'recent_risks': recent_risks_data
        })


class ApiRiskTreatmentViewSet(viewsets.ViewSet):
    """
    ViewSet for ApiRiskTreatment model
    """
    def list(self, request, risk_pk=None):
        try:
            risk = ApiRisk.objects.get(pk=risk_pk)
            treatments = ApiRiskTreatment.objects.filter(risk=risk)
            serializer = ApiRiskTreatmentSerializer(treatments, many=True)
            return Response(serializer.data)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, risk_pk=None, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=risk_pk)
            treatment = ApiRiskTreatment.objects.get(pk=pk, risk=risk)
            serializer = ApiRiskTreatmentSerializer(treatment)
            return Response(serializer.data)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
        except ApiRiskTreatment.DoesNotExist:
            return Response({"error": "Treatment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request, risk_pk=None):
        try:
            risk = ApiRisk.objects.get(pk=risk_pk)
            serializer = ApiRiskTreatmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(risk=risk)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, risk_pk=None, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=risk_pk)
            treatment = ApiRiskTreatment.objects.get(pk=pk, risk=risk)
            serializer = ApiRiskTreatmentSerializer(treatment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
        except ApiRiskTreatment.DoesNotExist:
            return Response({"error": "Treatment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, risk_pk=None, pk=None):
        try:
            risk = ApiRisk.objects.get(pk=risk_pk)
            treatment = ApiRiskTreatment.objects.get(pk=pk, risk=risk)
            treatment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ApiRisk.DoesNotExist:
            return Response({"error": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
        except ApiRiskTreatment.DoesNotExist:
            return Response({"error": "Treatment not found"}, status=status.HTTP_404_NOT_FOUND) 