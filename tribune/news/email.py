from django.core.mail import EmailMultiAlternatives  # django mail module to send emails 
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    #Creating message subject and sender 
    subject = 'Welcome to the Moringa Tribune Newsletter'
    sender = 'james@moringaschool.com'

    #Pass in context variables
    text_content = render_to_string('email/newsemail.txt', {"name":name})
    html_content = render_to_string('email/newsemail.html', {"name": name})

    msg = EmailMultiAlternatives('subject', 'text_content','sender[receiver]')
    msg.attach_alternative(html_content, 'text/html')
    msg.send()