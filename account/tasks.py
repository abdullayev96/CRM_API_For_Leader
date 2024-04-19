from .models import *
from celery import shared_task
from datetime import datetime

from django.conf import settings

from django.core.mail import send_mail
import random



# @shared_task
# def send_otp_email(email):
#     subject = 'Your account verification email is'
#     otp  = random.randint(1000, 9999)
#     from_email = settings.EMAIL_HOST
#     message = f'This is Your  OTP {otp}'
#     recipient_list = [email]
#
#     send_mail(subject, message, from_email, recipient_list)
    # user_obj = User.objects.get(email=email)
    # user_obj.otp = otp
    # user_obj.save()



@shared_task
def send_otp_email(email):
    try:
       subject = 'Online bozor saytiga hush  kelibsiz'
       from_email = settings.EMAIL_HOST
       message = f"Assalamu alaykum  \n platformadan foydalanayotganizdan hursandmiz"
       recipient_list = [email]
       send_mail(subject, message, from_email, recipient_list)

       print("Send email")

    except Exception as e:
              print(e)

# subject = "Online bozor saytiga hush  kelibsiz"
# message = f"Assalamu alaykum {user.username} \n platformadan foydalanayotganizdan hursandmiz"
#
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [user.email,]
#
# send_mail(subject, message, email_from, recipient_list)
#
#




@shared_task
def my_task():
   for i in range(2000000):
    print(i)

