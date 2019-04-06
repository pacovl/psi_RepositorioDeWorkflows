
from django.contrib import admin
from data.models import Category, Workflow

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Workflow, WorkflowAdmin)
