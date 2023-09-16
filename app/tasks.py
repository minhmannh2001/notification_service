from celery import shared_task
from flask import render_template
from helpers.utils import send_email
from flask import current_app


@shared_task()
def send_confirmation_mail(username, email, verification_link):
    mail = current_app.extensions["mail"]
    message = "Welcome to Discover Quests - Registration Successful"
    html = render_template('email_templates/registration_confirmation.html',
                           username=username,
                           email=email,
                           verification_link=verification_link)
    send_email(mail, message, [email], html)


@shared_task()
def send_password_reset_mail(username, email, reset_link):
    mail = current_app.extensions["mail"]
    message = "Discover Quests - Password Reset Request"
    html = render_template('email_templates/password_reset.html',
                           username=username,
                           reset_link=reset_link)
    send_email(mail, message, [email], html)


@shared_task()
def send_verification_mail(username, email, verification_link):
    mail = current_app.extensions["mail"]
    message = "Discover Quests - Email Verification Request"
    html = render_template('email_templates/email_verification.html',
                           username=username,
                           verification_link=verification_link)
    send_email(mail, message, [email], html)
