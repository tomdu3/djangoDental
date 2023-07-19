from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email;
			['tomduk@gmail.com'], # to email
			fail_silently=False,
			)
		messages.success(request, 'The email was sent successfully!')

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		# return the page
		return render(request, 'contact.html', {})
