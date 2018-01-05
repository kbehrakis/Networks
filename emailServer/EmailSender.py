from socket import *
# Get input from user
sender = '<'+raw_input('What email address is SENDING this message? ')+'>\r\n'
recipient = '<'+raw_input('What email address is RECEIVING this message? ')+'>\r\n'
subject = raw_input('Subject: ')+'\r\n'
msg = '\r\n'+raw_input('Please enter your message: ')
endmsg = '\r\n.\r\n'

wantToSpoof = raw_input('\r\nWould you like to spoof as someone else? (y/n) ')
if wantToSpoof == 'y':
    nameSpoofSender = raw_input('Enter the NAME of the person you would like to spoof as: ')
    emailOfSpoof = '<'+raw_input('What email address are you SPOOFING as? ')+'>\r\n'


print('\r\nMESSAGE PREVIEW: ')
print('\r\nTO: %s' % recipient)
if wantToSpoof == 'y':
    print('\r\nFROM: '+nameSpoofSender+emailOfSpoof)
else:
    print('\r\nFROM: %s' % sender)
print('\r\nSUBJECT: %s' % subject)
print('\r\n\r\nMESSAGE: %s' % msg)

readyToSend = raw_input('\r\nReady to send your message? (y/n) ')
if readyToSend == 'n':
    quit()

# Choose a mail server (e.g. Google mail server) and call it mailserver.
mailserver = 'ALT2.ASPMX.L.GOOGLE.COM'
port = 25

# Create socket called clientSocket
clientSocket = socket(AF_INET, SOCK_STREAM)
# and establish a connection with the mailserver
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024)
print recv       # Must have line break here, else syntax is wrong (spacing)
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)

# Get back and print the response
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
mailFrom = sender #'<kbehraki@wellesley.edu>\r\n'
clientSocket.send("MAIL FROM: "+mailFrom)
     # Copied directly from above to print
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send RCPT TO command and print server response.
mailTo =  recipient   # '<kbehraki@wellesley.edu>\r\n'
clientSocket.send("RCPT TO: "+mailTo)
     # Copied directly from above to print
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'


# Send DATA command and print server response.
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
    print '354 reply not received from server.'

# Send message data.
messageData = msg
    # Message ends with a single period.
markEnding = endmsg

if wantToSpoof == 'y':
    FROM = nameSpoofSender+emailOfSpoof
else:
    FROM = sender

TO = recipient

clientSocket.send("FROM: "+FROM+"TO: "+TO+"SUBJECT: "+subject+messageData+markEnding)

recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server'


# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
print quitCommand
clientSocket.send(quitCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
    print '221 reply not received from server'

print '\r\nMessage  has been sent!\r\n'
