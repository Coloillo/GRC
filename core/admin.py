from django.contrib import admin
from .models import Framework, Control, Evidence

# Register your models here.
@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'created_at', 'updated_at')
    list_filter = ('version', 'created_at')
    search_fields = ('name', 'description', 'version')

@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'title', 'framework')
    list_filter = ('framework',)
    search_fields = ('identifier', 'title', 'description')

@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'control', 'created_by', 'created_at')
    list_filter = ('control__framework', 'created_at')
    search_fields = ('title', 'description', 'control__identifier')
