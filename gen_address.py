#!/user/bin/ven python
# coding=utf-8

content = ''
addr = '"2cedcab10b06a5840f3d88508937abf097dc256e",'
for x in range(500):
    content += addr
content = '[' + content + ']'

with open('addresses.txt', 'w') as f:
    f.write(content)
