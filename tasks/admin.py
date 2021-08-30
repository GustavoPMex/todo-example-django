from django.contrib import admin
from .models import tasksModel

# Register your models here.

class tasksAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )

admin.site.register(tasksModel, tasksAdmin)