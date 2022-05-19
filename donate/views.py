from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Profile
from .models import Donation, Transaction
from django.conf import settings
from credo.payment import Payment
from django.contrib import messages
import random
import string
from django.http import HttpResponseRedirect

def welcome(request):
	'''this function is to redirect from login page to workspace list passing the username 
	of the logged in user as a parameter'''
	username = request.user.username
	if username == '':
		return render(request, 'account/landingPage.html', {'title': 'dropacoin'})
	else:
		return redirect('dashboard', username)


def dashboard(request, username, *args, **kwargs):
	user = get_object_or_404(User, username=username)
	donee_profile = Profile.objects.get(user=user)
	if request.method == 'POST':
		radio_amount = request.POST.get('inlineRadioOptions')
		custom_amount = request.POST.get('custom')
		message=request.POST.get('message')
		donor = request.user
		if custom_amount:
			amount = int(custom_amount)
		elif radio_amount:
			amount = int(radio_amount)

		if amount >=1 and donor.profile.account_balance >= amount:
			Donation.objects.create(
				user=donor,
				message=message,
				amount=amount,
				donated_to=user)

			donor_profile = get_object_or_404(Profile, user=donor)
			donor_profile.account_balance -= amount
			donee_profile.account_balance += amount
			donee_profile.fans.add(donor)
			donor_profile.save()
			donee_profile.save()
	
	context = {
		'profile': donee_profile,
	}	
	return render(request, 'donate/dashboard.html', context)


def random_char():
       return ''.join(random.choice(string.ascii_letters) for x in range(5))


def get_amount(request, username):
	user = get_object_or_404(User, username=username)
	profile = get_object_or_404(Profile, user=user)

	if request.method == 'POST':
		amount = request.POST.get('amount')
		customer_name = f"{user.first_name} {user.last_name}"
		slug = random_char()

		payment = Payment(public_key=settings.CREDO_PUBLIC_KEY, secret_key=settings.CREDO_SEC_KEY)
		

		# to initiate a payment
		transaction = Transaction.objects.create(user=user, amount=amount)
		status, new_payment = payment.initiate_payment(
			amount=amount, 
			currency='NGN', 
			customer_name=customer_name,
			customer_email=user.email,
			customer_phone='23480123456789',
			trans_ref=slug+str(transaction.id), 
			payment_options='CARD,BANK',
			redirect_url=f"https://dropacoinn.herokuapp.com/verify_funds/?q={slug}{transaction.id}"
			)

		if status == 200:
			# profile.pending += amount
			# profile.save()
			payment_url = new_payment["paymentLink"]
			return HttpResponseRedirect(payment_url)
		
	context = {
		'user': user,
		}	

	return render(request, 'donate/get_amount.html', context)




def verify_funds(request, *args, **kwargs):
	query = request.GET.get("q")
	id_ = query[5:]
	print("vjdjsjskdskdjsd verify")
	payment = Payment(public_key=settings.CREDO_PUBLIC_KEY, secret_key=settings.CREDO_SEC_KEY)
	
	status, verify_payment = payment.verify_payment(transaction_reference=query)
	if status == 200:
		transaction = get_object_or_404(Transaction, pk=id_)
		transaction.status=True
	
		profile = get_object_or_404(Profile, user=transaction.user)
		profile.account_balance += transaction.amount
		profile.save()
		transaction.save()
		print("jfjjfjfj ending")
		messages.success(request,'Account has been successfull funded')
		return redirect('landing_page')
	else:
		print("jfjfjf error")
		messages.warning(request,'There was error processing your payment')
		return redirect('landing_page')



