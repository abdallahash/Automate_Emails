#SMTP :  Simple Main Transfer Protocall.
#Protocall that we need to follow to send emails
import smtplib
import pandas as pd
from email.mime.text import MIMEText 
import email.utils 
import codecs 

sender_email = 'abdallah.sender@gmail.com'
sender_name = 'Abdallah Ashraf'

password = 'Never_Stop123'

csv_file = 'Email_list.csv'

email_list = pd.read_csv(csv_file, sep=',')

# for name, email in zip(email_list['name'], email_list['email']):
#     print("Email sent to {} at {}".format(name, email))


recipient_emails = email_list['email']
recipient_names = email_list['name']

# html_file = codecs.open('Email_content.html', 'r')

# email_html = html_file.read()
# print(email_html)

with open('Email_content.html', 'r') as f:

    email_html = f.read()
print(email_html)

def send_email():
    print("\n Broadcasting email...\n")
    for recipient_name, recipient_email in zip(recipient_names, recipient_emails):

        message = MIMEText(email_html.format(recipient_name), 'html')
        message.add_header('Content-Type', 'text/html')

        message['To'] = email.utils.formataddr((recipient_name, recipient_email))
        message['From'] = email.utils.formataddr((sender_name, sender_email))
        message['Subject'] = 'My Upwork client story'
    
        #set up the email server for Gmail and use a commen port()
        server = smtplib.SMTP('smtp.gmail.com', 587)

        #Turn on Transport Layer Security, Every thing afer this will be encrypted
        server.starttls()

        server.login(sender_email, password)

        #sending email
        server.sendmail(sender_email, recipient_email, message.as_string())

        server.quit()

        print("\n\n Email sent to {} at {}".format(recipient_name, recipient_email))
    print('Brodcasting emails done.')

send_email()
