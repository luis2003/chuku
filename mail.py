import smtplib
import ssl


def send_email(body_text):
    # port = 587
    port = 1025
    # smtp_server = 'smtp-relay.sendinblue.com'
    smtp_server = 'localhost'
    password = 'a6BpGd8Ymr0DTkVn'

    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email = "luis2003.dev@gmail.com"
    receiver_email = "luis2003@gmail.com"
    message = """\
    From: {}
    To: {}
    Subject: reporte variacion de cryptos (USDT en binance)
    
    {}
    
    Correo enviado desde Python.""".format(sender_email, receiver_email, body_text)

    with smtplib.SMTP(smtp_server, port) as server:
        try:
            server.ehlo()
            # server.starttls(context=context)
            # server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            print(e)
        finally:
            server.quit()
