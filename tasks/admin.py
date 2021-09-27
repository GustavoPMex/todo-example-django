from django.contrib import admin
from .models import tasksModel

# Register your models here.

class tasksAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )

    def get_changeform_initial_data(self, request):
        get_data = super(tasksAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        get_data['status'] = True
        return get_data

admin.site.register(tasksModel, tasksAdmin)