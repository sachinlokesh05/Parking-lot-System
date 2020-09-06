# Create your tasks here
from __future__ import absolute_import, unicode_literals
from parking_system.settings import EMAIL_HOST_USER
from celery import shared_task
from parking_system.celery import app as  celery_app
from django.core.mail import  EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task(serializer='json')
def send_mail_system(**kwargs):
    email_from = EMAIL_HOST_USER
    recipient_email = kwargs.get('recepients')
    mail_subject = kwargs.get('subject')
    mail_message = render_to_string(kwargs['template_name'], {
                        'user':  kwargs.get('vehicle_owner',None),
                        'start_time':kwargs.get('start_time',None),
                        'vehicle_number':kwargs.get('vehicle_number',None),
                        'slot':kwargs.get('vehicle_slot',None),
                        'charges':kwargs.get('charges',None),
                    })
    subject, from_email, to = mail_subject, email_from, recipient_email
    msg = EmailMultiAlternatives(subject, mail_message, from_email, [to])
    msg.attach_alternative(mail_message, "text/html")
    msg.send()