import json

def contacts():
    email = []
    with open('utils/contacts.json') as f:
        data = json.load(f)
        for i in data['contatos']:
            email.append(i['email'])
    return email
