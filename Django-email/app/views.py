from django.http import HttpResponse
from django.shortcuts import render , redirect
from templated_email import send_templated_mail , get_templated_mail , InlineImage
import os
from django.conf import settings



def send_email(request):
    
    send_templated_mail(
            template_name='welcome',
            from_email='from@example.com',
            recipient_list=['to@example.com'],
            context={
                'username':"bishal",
                'full_name': "bishal",
                'signup_date': "bishal",
                'logo': 'logo/logo.png'
            }
    ) 
    return HttpResponse("Email sent successfully")


def get_email(request):
    
    context = {
        'username':"bishal",
        'full_name': "bishal",
        'signup_date': "bishal",
        "logo": "logo/logo.png"
    }
    return render(request, "templated_email/welcome.email", context)