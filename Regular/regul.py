import re

pattern = r"[rR][bB]+[rR]"
test = ['sRbBr', 'rbbr', 'qwerbbR', 'text', 'textRBR']
for text in test:
    if re.findall(pattern, text):
        print(f'match in {text}')