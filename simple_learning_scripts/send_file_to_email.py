'''
ABOUT: THIS IS A PYTHON SCRIPT THAT CAN BE USED TO SEND FILES FROM A LOCAL SOURCE TO email recipents
       IT CAN BE USED IN CICD PIPELINES OR EVEN ANY PROCESS
       JUST HELPS AUTOMATE THE PROCESS
'''
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_to_email():
  mail_list = [] #list of email recipients

  for mail in mail_list:
    email_username = os.environ.get('EMAIL_USERNAME') # email sender email
    email_passwd = os.environ.get('EMAIL_PASSWD') #email sender passwd

    username = f"{email_username}"
    password = f"{email_passwd}"
    mail_from = f"{email_username}"
    mail_subject = f"{email subject}" # subject of email
    mail_body = "HELLO, THIS IS A SAMPLE EMAIL" # email body in text format
    mail_attachment=f"{src_file}" # local file to be added as attachment
    mail_attachment_name=f"{src_file}" # name of attachment as shown in email

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))

    with open(mail_attachment, "rb") as attachment:
        mimefile = MIMEBase('application', 'octet-stream')
        mimefile.set_payload((attachment).read())
        encoders.encode_base64(mimefile)
        mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
        mimemsg.attach(mimefile)
        connection = smtplib.SMTP(host='smtp.office365.com', port=587)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(mimemsg)
        connection.quit()

send_to_email()
