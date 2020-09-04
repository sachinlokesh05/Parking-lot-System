from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .tasks import send_mail_system
class EmailClass():
    @classmethod
    def send_email(cls, **kwargs):
        return send_mail_system.delay(**kwargs)

