from django.db import models
from django.contrib.auth.models import User

class Risk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class RiskAssessment(models.Model):
    IMPACT_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    LIKELIHOOD_CHOICES = [
        ('RARE', 'Rare'),
        ('UNLIKELY', 'Unlikely'),
        ('POSSIBLE', 'Possible'),
        ('LIKELY', 'Likely'),
        ('CERTAIN', 'Certain'),
    ]

    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='assessments')
    impact = models.CharField(max_length=10, choices=IMPACT_CHOICES)
    likelihood = models.CharField(max_length=10, choices=LIKELIHOOD_CHOICES)
    mitigation_plan = models.TextField()
    status = models.CharField(max_length=20, default='OPEN')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assessments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Assessment for {self.risk.title}"

    @property
    def risk_level(self):
        impact_scores = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3, 'CRITICAL': 4}
        likelihood_scores = {'RARE': 1, 'UNLIKELY': 2, 'POSSIBLE': 3, 'LIKELY': 4, 'CERTAIN': 5}
        
        score = impact_scores[self.impact] * likelihood_scores[self.likelihood]
        
        if score <= 4:
            return 'LOW'
        elif score <= 8:
            return 'MEDIUM'
        elif score <= 12:
            return 'HIGH'
        else:
            return 'CRITICAL'
