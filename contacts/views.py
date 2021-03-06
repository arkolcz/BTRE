from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry on that house')
                return redirect('/listings/' + listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                         phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Inquiery',
            'Contact requested for ' + listing + '.',
            'dummy@dummy.com',
            [realtor_email, 'dummy@dummy.com'],
            fail_silently=False
        )

        messages.success(request, 'You request has been sent')
        return redirect('/listings/' + listing_id)


