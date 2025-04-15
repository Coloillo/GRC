from django.contrib import admin
from .models import Risk, RiskAssessment

# Register your models here.
@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'category')

@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ('risk', 'impact', 'likelihood', 'risk_level', 'status', 'assigned_to')
    list_filter = ('impact', 'likelihood', 'status')
    search_fields = ('risk__title', 'mitigation_plan')
