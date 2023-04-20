from service import sendmail
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mail_user', required=True)
parser.add_argument('--mail_pass', required=True)

args = parser.parse_args()
e_user = args.mail_user
e_pass = args.mail_pass

def main():

    sendmail.enviar_email(e_user, e_pass)

if __name__ == '__main__':
    main()