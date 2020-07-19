from django.contrib import admin
from .models import *
from django.db import models
from tinymce.widgets import TinyMCE

#Override Project class to put some features into it
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Title",{"fields":["title"]}),
            ("Technologies", {"fields": ["technology"]}),
            ("Content",{"fields":["description"]}),
            ("Images", {"fields": ["image"]}),
        ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

# Register your models here.
admin.site.register(Project,ProjectAdmin)