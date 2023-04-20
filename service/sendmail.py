import smtplib
import email.message
from service import contacts
import logging

def enviar_email(user, passwd): 
    corpo_email = """
    <p>MENSAGEM EM FORMATO HTML</p>
	<p>MENSAGEM EM FORMATO HTML</p>
    """

    try:
        recept = contacts.contacts()
    except Exception as e:
        logging.warning('Erro ao buscar contatos: {}'.format(e))
        exit(1)
    
    for send in recept:
        try:
            logging.warning('Enviando email para: {}'.format(send))
        
            msg = email.message.Message()
            msg['Subject'] = "Disco do FileSender"
            msg['From'] = '{}'.format(user)
            msg['To'] = '{}'.format(send)
            password = '{}'.format(passwd) 
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email )

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            logging.warning('Email enviado para: {}'.format(send))
        except Exception as e:
            logging.warning('Erro ao enviar para email: {}'.format(send))

