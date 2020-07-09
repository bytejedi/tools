#!/user/bin/ven python
# coding=utf-8

address_count = 100
address = 'TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL'


def gen_addresses(count, addr=address):
    addr = '"' + addr + '",'
    content = ''
    for x in range(count):
        content += addr
    content = content[:-1]
    return '[' + content + ']'


with open('addresses.txt', 'w') as f:
    f.write(gen_addresses(address_count, address))
