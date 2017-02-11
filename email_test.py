import sys
import imaplib
import pyttsx
import os
import getpass
import email
import datetime
from inspect import getmembers
from pprint import pprint
reload(sys)  
engine = pyttsx.init()
sys.setdefaultencoding('utf8')
EMAIL_ACCOUNT = "rockingraj2026@gmail.com"
EMAIL_FOLDER = "INBOX"
fopen = open('results.txt', 'w')
number_of_mails = 0
def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """
    i = 0
    rv, data = M.search(None,'(SINCE "25-Dec-2016" SUBJECT "airtel")')
    if rv != 'OK':
        print "No messages found!"
	return
	myfile = open('results.txt', 'w')
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        decode = email.Header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
        print 'Message %s: %s' % (num, subject.encode('utf-8'))
        print 'Raw Date:', msg['Date']
        print "test"
        #msg = str(msg['Body'])[0]
        #pprint(getmembers(msg))
        i=i+1
        global number_of_mails
        number_of_mails = i
        fopen.write("%d)"%i)
        fopen.write(subject)
        fopen.write("\n")
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print "Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S")
		

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    rv, data = M.login(EMAIL_ACCOUNT, '9773501562')
except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "
print rv, data
rv, mailboxes = M.list()
if rv == 'OK':
    print "Mailboxes:"
    print mailboxes

rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    print "Processing mailbox...\n"
    process_mailbox(M)
    M.close()
else:
    print "ERROR: Unable to open mailbox ", rv

engine.say('Hello Sir, You have %d new mails for the day'%number_of_mails)
engine.runAndWait()
fopen.close()
M.logout()
	
#import imapclient
#from backports import ssl
#imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login('rockingraj2026@gmail.com', '')