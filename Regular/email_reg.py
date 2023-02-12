import re
def email_validate(email: str):
    email_pattern = r'[a-zA-Z0-9]*(-?\.?[_a-zA-Z0-9])*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*'
    if re.match(email_pattern, email):
        return email
    return 'Email is not validate'


emails = ['toxa270400@gmail.com']

with open('test1.txt', 'a') as f:
    for text in emails:
        f.writelines(email_validate(text) + '\n')
