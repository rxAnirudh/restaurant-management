import logging
import smtplib
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message
from django.conf import settings
from jinja2 import Environment

def detectUser(user):
    if user.role == 1:
        redirectUrl = 'vendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl

CHARSET = "UTF-8"
port  = 25
password = "Radixweb@13"
smtp_server = "192.168.100.101"
SENDER_EMAIL="anirudh.chawla@radixweb.com"

class EmailManager:
    """Class for managing email"""
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    def __init__(self) -> None:
        try:
            self.server.login(SENDER_EMAIL,password)
        except Exception as e:
            logging.debug(e)

    def send_email(self,request, user, subject,template):
        """Function for sending email"""
        try:
            from_email = settings.DEFAULT_FROM_EMAIL
            current_site = get_current_site(request)
            message = render_to_string(template, {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            mail = EmailMessage(subject, message, from_email, to=[to_email])
            message = EmailMessage()
            message.add_alternative(Environment().from_string(template).render(
                    title='Hello World!'
                ))
            self.server.sendmail(SENDER_EMAIL, to_email, message.as_string())
            s = smtplib.SMTP('localhost')
            s.send_message(message)
            s.quit()

            return {
                "message": "Email has been sent successfully on your email address",
                "status": True
            }
        except Exception as exception:
            print(exception)
            return {
                "error": "Error while sending an email",
                "status": False
            }
    
    def send_verification_email(self,request, user, mail_subject, email_template):
        try:
            from_email = settings.DEFAULT_FROM_EMAIL
            current_site = get_current_site(request)
            message = render_to_string(email_template, {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            message = EmailMessage(mail_subject, message, from_email, to=[to_email])
            # message.add_alternative(Environment().from_string(email_template).render(
            #         title='Hello World!'
            #     ))
            self.server.sendmail(SENDER_EMAIL, to_email, message.as_string())
            s = smtplib.SMTP('localhost')
            s.send_message(message)
            s.quit()

            return {
                "message": "Email has been sent successfully on your email address",
                "status": True
            }
        except Exception as exception:
            print(exception)
            return {
                "error": "Error while sending an email",
                "status": False
            }


def send_notification(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(mail_template, context)
    if(isinstance(context['to_email'], str)):
        to_email = []
        to_email.append(context['to_email'])
    else:
        to_email = context['to_email']
    mail = EmailMessage(mail_subject, message, from_email, to=to_email)
    mail.content_subtype = "html"
    mail.send()
