from django.db import models
from django.contrib.auth.models import User

def get_name(self):
    return '{} {}'.format(self.last_name, self.first_name)
User.add_to_class("__str__", get_name)

class Group(models.Model):
	group_name = models.CharField(max_length=256,null=False, verbose_name='物品名稱')

	def __str__(self):
		return self.group_name

class Equipment(models.Model):
	group_name = models.ForeignKey(Group, verbose_name='設備')
	item_no = models.PositiveIntegerField(default=1, verbose_name='物品序號')
	yaer = models.CharField(max_length=256,null=False, verbose_name='採購年度')
	location = models.CharField(max_length=256,null=False, verbose_name='使用地點')
	unit = models.CharField(max_length=256,null=False, verbose_name='使用單位')
	notation = models.TextField(max_length=512, blank=True, verbose_name='備註')
	equip_code = models.BooleanField(default=True)

	def __str__(self):
		return '{} {} {}'.format(self.item_no, self.group_name, self.notation)


class Loan(models.Model):
	user = models.ForeignKey(User, verbose_name='使用者')
	group_name = models.ForeignKey(Group, verbose_name='物品名稱')
	loan_date = models.DateField(auto_now_add=True, verbose_name='歸還日期')
	return_date = models.DateField(default='9999-01-01')
	return_code = models.BooleanField(default=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True) 
	notation = models.TextField(max_length=512, blank=True, verbose_name='備註')

	def __str__(self):
		return str(self.pk)