from django.contrib import admin
from .models import Session, Version, Section

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_code', 'session', 'institution', 'branch', 'status', 'created_by', 'created_at')
    search_fields = ('session_code', 'session', 'institution', 'branch')
    list_filter = ('status', 'created_at')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_code', 'version', 'status', 'created_at', 'updated_by', 'updated_at')
    search_fields = ('version_code', 'version')
    list_filter = ('status', 'created_at', 'updated_at')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_code', 'section', 'institution', 'branch', 'status', 'created_at')
    search_fields = ('section_code', 'section', 'institution', 'branch')
    list_filter = ('status', 'created_at')
