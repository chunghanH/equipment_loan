from django import forms
from loan_app.models import Loan
class LoanForm(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ('group_name', 'notation')
		