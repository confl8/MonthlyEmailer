# Import correct library for sending emails
import smtplib

fromaddr = 'replacewithyouremail@gmail.com'
toaddrs  = 'recipient1@gmail.com', 'recipient2@gmail.com',
'etcetera@gmail.com'
msg = 'This is where your message goes, in bewteen thise quotations'


# Credentials (if needed)
username = 'yourloginemail@gmail.com'
password = 'yourpassword'

# The actual mail send, don't change any of this
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

# Note: You WILL have to permit Gmail to send these, otherwise
# You'll just receive an error. Turn on "less secure apps"
# Here : https://www.google.com/settings/security/lesssecureapps
