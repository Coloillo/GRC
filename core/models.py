from django.db import models
from django.contrib.auth.models import User

class Framework(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    version = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} v{self.version}"

class Control(models.Model):
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name='controls')
    identifier = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['framework', 'identifier']

    def __str__(self):
        return f"{self.framework.name} - {self.identifier}: {self.title}"

class Evidence(models.Model):
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='evidence')
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='evidence/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Evidence for {self.control.identifier}: {self.title}"
