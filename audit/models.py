from django.db import models
from django.contrib.auth.models import User
from core.models import Control

class Audit(models.Model):
    AUDIT_TYPE_CHOICES = [
        ('INTERNAL', 'Internal Audit'),
        ('EXTERNAL', 'External Audit'),
        ('COMPLIANCE', 'Compliance Audit'),
        ('SECURITY', 'Security Audit'),
        ('OPERATIONAL', 'Operational Audit'),
    ]
    
    STATUS_CHOICES = [
        ('PLANNED', 'Planned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    audit_type = models.CharField(max_length=20, choices=AUDIT_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNED')
    start_date = models.DateField()
    end_date = models.DateField()
    lead_auditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_audits')
    auditors = models.ManyToManyField(User, related_name='assigned_audits')
    controls = models.ManyToManyField(Control, related_name='audits')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_audits')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
class AuditFinding(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_REMEDIATION', 'In Remediation'),
        ('REMEDIATED', 'Remediated'),
        ('VERIFIED', 'Verified'),
        ('CLOSED', 'Closed'),
        ('ACCEPTED', 'Risk Accepted'),
    ]
    
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name='findings')
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='findings', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    remediation_plan = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_findings')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_findings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.audit.title} - {self.title}"
        
class AuditEvidence(models.Model):
    finding = models.ForeignKey(AuditFinding, on_delete=models.CASCADE, related_name='evidence')
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='audit_evidence/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Evidence for {self.finding.title}: {self.title}"
