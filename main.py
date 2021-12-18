import yagmail
import os
import time

sender = 'dan.nelson1@gmail.com'
receiver = 'ygqchvvz@netmail.tk'
subject = 'This is the subject of the email.'
content = '''
This is the content of the email
'''
while True:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email sent")
    time.sleep(60)
