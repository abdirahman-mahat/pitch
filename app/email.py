from flask_mail import Message
from flask import render_template
from . import mail
<<<<<<< HEAD

def mail_message(subject,template,to,**kwargs):
   sender_email = 'lewismutuma1000@gmail.com'

   email = Message(subject, sender=sender_email, recipients=[to])
   email.body= render_template(template + ".txt",**kwargs)
   email.html = render_template(template + ".html",**kwargs)
   mail.send(email)
=======
def mail_message(subject,template,to,**kwargs):
    sender_email = abdirahmanmahat3@gmail.com

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
