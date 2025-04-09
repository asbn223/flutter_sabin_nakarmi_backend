from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_account_forgot_password_email(user, otp):
    subject = 'Your OTP for Password Reset'
    html_message = render_to_string('forgot_password_template.html',
                                    {'user': user, 'otp': otp,}
                                    )
    plain_message = strip_tags(html_message)  # Plain text version of the email
    from_email = settings.DEFAULT_FROM_EMAIL  # Your email address
    recipient_list = [user.email]  # The recipient's email

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False,)
