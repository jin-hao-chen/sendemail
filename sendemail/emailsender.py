# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender(object):

    def __init__(self, sender, password, receiver, host='smtp.163.com'):
        self.sender = sender
        self.sender_email = sender + '@' + '.'.join(host.split('.')[1:])
        self.password = password
        self.host = host
        if isinstance(receiver, str):
            receiver = [receiver]
        self.receiver = receiver

    def send(self, msg):
        try:
            server = smtplib.SMTP_SSL(host=self.host, port=465)
            server.connect(self.host)
            server.login(self.sender, self.password)
            server.sendmail(self.sender_email, self.receiver, msg.as_string())
            server.quit()
            print('finish sending email to {self.sender}')
        except Exception as e:
            print(e)

    @property
    def receiver(self):
        return self.receiver

    @receiver.setter
    def receiver(self, receiver):
        if isinstance(receiver, str):
            receiver = [receiver]
        self.receiver = receiver

    def make_msg(self, subject, date, content):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = self.receiver[0]
        msg['Date'] = date
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        return msg
