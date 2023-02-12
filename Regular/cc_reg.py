import re

test = ['4444-1111-2222-3333',
        '5555-4444-3333-2222',
        '3333-5555-4444-1111',
        '6666-3333-2222-5555',
        '7777-2222-1111-4444',
        '8888-1111-4444-3333',
        '1111-6666-7777-8888',
        '2222-5555-8888-3333',
        '5555-2222-1111-6666',
        '4444-3333-7777-9999']


def credit_card_validate(card: str):
    credit_card_pattern = r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}'
    if re.match(credit_card_pattern, card):
        return card
    return 'Card is not validate'


with open('test.txt', 'a') as f:
    for text in test:
        f.writelines(credit_card_validate(text) + '\n')