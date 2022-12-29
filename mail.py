import smtplib, ssl

port = 587
smtp_server = 'smtp-relay.sendinblue.com'
password = 'a6BpGd8Ymr0DTkVn'

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "luis2003.dev@gmail.com"
receiver_email = "luis2003@gmail.com"
message = """\
From: {}
To: {}
Subject: Hi there

This message is sent from Python.""".format(sender_email, receiver_email)


with smtplib.SMTP(smtp_server, port) as server:
    try:
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()
