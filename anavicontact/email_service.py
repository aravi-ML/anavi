from django.core.mail import send_mail,send_mass_mail,mail_admins


class EmailService:
    def __init__(self):
        pass

    def send_email(self,sender,receiver_list,data=None):
        """ @sender is the name of person who send email, 
            @receiver list is a l ofist person who will receive message
            @data["sender_email"] contain the meail of sender 
            @data["password"] is the authentification password
            @data["subject"] contain the subject of message
            @data["msg"] contain the message of the mail """
            
        if(data["sender_email"]=="araviml3@gmail.com"):
            password="998521ANAVI"
        elif(data["sender_email"]=="pecole-noreply@protogons.com"):
            password=""
        else:
            password=data["998521ANAVI"]
        try:
            send_mail(
                  subject=data["subject"],
                  message=data["msg"],
                  from_email=data["sender_email"],
                  recipient_list=receiver_list,
                  auth_user=data["sender_email"],
                  auth_password=password,
                  html_message=data["msg"])
        except Exception as e:
            pass