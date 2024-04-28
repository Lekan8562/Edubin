from django.contrib import admin
from .models import CustomUser,School,Department
# Register your models here.

admin.site.register(CustomUser)
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}