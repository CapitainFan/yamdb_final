from rest_framework_simplejwt.tokens import AccessToken
from django.core.mail import EmailMessage
from django.conf import settings


def send_email(email, confirmation_code):
    email = EmailMessage(
        subject=settings.SUBJECT,
        from_email=settings.DEFAULT_FROM_EMAIL,
        body=confirmation_code,
        to=[email, ]
    )
    email.send(fail_silently=False)


def get_tokens_for_user(user):
    access = AccessToken.for_user(user)
    return str(access)
