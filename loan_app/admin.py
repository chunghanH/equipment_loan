from django.contrib import admin
from loan_app import models

class LoanAdmin(admin.ModelAdmin):
	list_display  = ['user','group_name','loan_date','return_date']

class GroupAdmin(admin.ModelAdmin):
	search_fields = ['group_name']
	list_display = ['group_name']
	list_display_links = None
	list_editable  = ['group_name']

class EquipmentAdmin(admin.ModelAdmin):
	search_fields = ['item_no','group_name','yaer','location','unit','location']
	list_display = ['item_no','group_name','yaer','location','unit','location']
	list_display_links = None
	list_editable = ['item_no','group_name','yaer','location','unit','location']
	
# Register your models here.
admin.site.register(models.Loan, LoanAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Group, GroupAdmin)
