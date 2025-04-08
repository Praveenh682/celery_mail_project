from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, recipient_list):
    print('yessss')
    send_mail(
        subject,
        message,
        'praveenvpk0802@gmail.com', 
        recipient_list,
        fail_silently=False,
    )
    print('qwert')
    return "Email Sent"
