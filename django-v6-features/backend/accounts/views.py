from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.tasks import task

# Create your views here.

def register(request):
    return HttpResponse("registser page")


@task
def email_users(emails, subject, message):
    return send_mail(subject, message, None, emails)