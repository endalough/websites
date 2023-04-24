from django.contrib import admin
from .models import Todo

#Class to make the created date field visible in admin page
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    

# Register your models here.
admin.site.register(Todo, TodoAdmin)
