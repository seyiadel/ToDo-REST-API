from django.contrib import admin
from api.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=['title','description','done','created_at']

admin.site.register(Todo, TodoAdmin)