import imaplib
import getpass
import email
mail = imaplib.IMAP4_SSL("imap.gmail.com")
password = getpass.getpass()
mail.login('rockingraj2026@gmail.com',password)
mail.list()
mail.select("inbox")
result,data = mail.search(None, "ALL")
ids = data[0] #This contains the list of ids
id_list = ids.split() #Split the list into individual mail 
latest_email_id = id_list[-1] #Get the latest email id
result, data = mail.fetch(latest_email_id , "(RFC822)")
raw_email = data[0][1] #This will output the entire body with html tags
email_message = email.message_from_string(raw_email)
print email_message['To']
print email.utils.parseaddr(email_message['From'])
print email_message['Subject']
print email_message.items()
def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


	
