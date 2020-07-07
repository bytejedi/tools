#!/user/bin/ven python
# coding=utf-8

from tronapi import Tron
from tronapi import HttpProvider

full_node = HttpProvider('https://api.shasta.trongrid.io')
solidity_node = HttpProvider('https://api.shasta.trongrid.io')
event_server = HttpProvider('https://api.shasta.trongrid.io')

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

print(tron.address.from_hex('41954c02e8bd2f81c58e1909447314a937f46b0f22'))
print(tron.address.to_hex('TE4mbZVHabhusvarxqwEESkVfxgViBrjEK'))
