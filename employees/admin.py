from django.contrib import admin
from employees.models import Employees,Department

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_filter = ['department']
    search_fields = ['email']


admin.site.register(Department)
admin.site.register(Employees, EmployeesAdmin)

