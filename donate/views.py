from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from account.models import Profile
from .models import Donation

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
	if request.method == 'POST':
		amount=request.POST['amount']
		message=request.POST['message']

		donor = request.user

		if amount >=50 and donor.profile.account_balance >= amount:
			Donation.objects.create(
				user=donor,
				message=message,
				amount=amount,
				donated_to=user)

			donor.profile.account_balance - amount
			user.profile.account_balance + amount
			donor.profile.save()
			user.profile.save()
	
	profile = Profile.objects.get(user=user)
	context = {
		'profile': profile,
	}	
	return render(request, 'donate/dashboard.html', context)


# from credo.direct_charge import DirectCharge









# direct_charge = DirectCharge(public_key='your-public-key', secret_key='your-secret-key')

# # Charge a card without 3DS verification
# status, charge_card = direct_charge.charge_card(
# 	amount=2000, 
# 	currency='NGN', 
# 	card_number='5204730000001003',
# 	expiry_month="12", 
# 	expiry_year="25",
# 	security_code="123",
# 	trans_ref="iy67f64hvc61",
# 	customer_email='random@mil.com',
# 	customer_phone="23480123456789", 
# 	customer_name='Random',
# 	payment_slug="0H0UOEsawNjkIxgsporr")