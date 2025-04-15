from django.contrib import admin
from .models import Project, Task, Milestone

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'start_date', 'end_date', 'project_manager')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('title', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'due_date', 'assigned_to')
    list_filter = ('status', 'priority', 'due_date')
    search_fields = ('title', 'description')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'description')
