from django.contrib import admin
from .models import Audit, AuditFinding, AuditEvidence

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('title', 'audit_type', 'status', 'start_date', 'end_date', 'lead_auditor')
    list_filter = ('audit_type', 'status', 'start_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('auditors', 'controls')

@admin.register(AuditFinding)
class AuditFindingAdmin(admin.ModelAdmin):
    list_display = ('title', 'audit', 'severity', 'status', 'due_date', 'assigned_to')
    list_filter = ('severity', 'status', 'audit')
    search_fields = ('title', 'description', 'remediation_plan')

@admin.register(AuditEvidence)
class AuditEvidenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'finding', 'created_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
