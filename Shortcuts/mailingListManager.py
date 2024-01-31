#--------------------- Mailing List Manager ------------------------
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict
from contextlib import suppress

def send_mail(subject,message,from_addr,*to_addr,host="localhost",port=1025,headers=None):
    headers = headers if headers else {}
    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value
    sender = smtplib.SMTP(host,port)
    for addr in to_addr:
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr,addr,email.as_string())
    sender.quit()


class MailingList:
    """Manage groups of email addresses for sending emails."""
    def __init__(self,data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self,email,group):
        self.email_map[email].add(group)

    def emails_in_groups(self,*groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails
    
    def send_mailing(self,subject,message,from_addr,*groups,headers=None):
        emails = self.emails_in_groups(*groups)
        send_mail(subject,message,from_addr,*emails,headers=headers)

    def save(self):
        with open(self.data_file,"w") as file:
            for email, groups in self.email_map.items():
                file.write(f"{email} {','.join(groups)}\n")

    def load(self):
        self.email_map = defaultdict(set)
        with suppress(IOError):
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(" ")
                    groups = set(groups.split(","))
                    self.email_map[email] = groups

    def __enter__(self):
        self.load()
        return self
    
    def __exit__(self,type,value,tb):
        self.save()


with MailingList("addresses.db") as ml:
    ml.add_to_group("friend1@example.com","friend")
    ml.add_to_group("friend2@example.com","friend")
    ml.add_to_group("family1@example.com","family")
    ml.add_to_group("pro1@example.com","professional")
    ml.send_mailing("A Party","Only friend and family","me@example.com","friend","family",headers={
        "Reply-To":"me@example.com"
    })

