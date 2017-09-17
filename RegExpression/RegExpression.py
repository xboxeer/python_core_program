import re

with open('SampleText.txt','r') as fout:
    source=fout.read()
    m=re.match('</?a href=[^>]+>',source,'m')
    print(m.groups())
    if m is not None:
        print(m.group())

