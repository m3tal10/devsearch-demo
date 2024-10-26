from django.core.mail import send_mail
from django.conf import settings
import os
class Email():
    def __init__(self):
        self.email_from = settings.DEFAULT_FROM_EMAIL

    def send_welcome_email(self,user_email):
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        recipient_list = [user_email]
        send_mail(subject, message, self.email_from, recipient_list, fail_silently=False)