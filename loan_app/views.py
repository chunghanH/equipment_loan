from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from loan_app.models import Loan, Equipment
from loan_app.form import LoanForm
from django.contrib import messages
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Min

@login_required
def loan_list(request):
	loans = loans = Loan.objects.all().order_by('-return_code','-loan_date')
	if not request.user.is_superuser and not request.user.is_staff:
		loans = Loan.objects.filter(user=request.user.pk).order_by('-return_code','-loan_date')

	paginator = Paginator(loans, 12)
	page = request.GET.get('page')
	try:
		loans = paginator.page(page)
		
	except PageNotAnInteger:
		loans = paginator.page(1)

	except EmptyPage:
		loans = paginator.page(paginator.num_pages)

	return render(request, 'loan_app/loan_list.html', context={'loans' : loans})

@login_required
def loan_detail(request,pk):
	loan = Loan.objects.get(pk=pk)
	return render(request, 'loan_app/loan_detail.html', context={'loan' : loan})

@login_required
def create_loan(request):
	form = LoanForm(request.POST or None)
	if form.is_valid():
		loan = form.save(commit=False)
		loan.user = request.user
		group_name = request.POST.get('group_name')
		equip_query_set = Equipment.objects.filter(pk=group_name, equip_code=True).annotate(Min('item_no'))
	
		if equip_query_set:
			equipment = get_object_or_404(Equipment, pk=equip_query_set)
			equipment.equip_code = False
			loan.save()
			equipment.save()
			return redirect('loan_app:list')
		else:
			messages.add_message(request, 50, '無庫存')

	return render(request, 'loan_app/loan_form.html', context={'form' : form})

@login_required
def return_action(request, pk):
	loan = get_object_or_404(Loan, pk=pk)
	loan.return_date = time.strftime('%Y-%m-%d', time.localtime())
	loan.return_code = False
	equipment = get_object_or_404(Equipment, pk=loan.group_name.pk)
	equipment.equip_code = True
	loan.save()
	equipment.save()
	return redirect('loan_app:list')

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user and user.is_active :
			login(request, user)
			return redirect('loan_app:list')
		else:
			messages.add_message(request, 50, '無效的帳號或密碼')

	return render(request, 'loan_app/user_login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('user_login.html')