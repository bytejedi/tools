#!/user/bin/ven python
# coding=utf-8

from tronapi import Tron
from tronapi import HttpProvider
import concurrent.futures
import time
from multiprocessing import Pool

full_node = HttpProvider('https://api.shasta.trongrid.io')
solidity_node = HttpProvider('https://api.shasta.trongrid.io')
event_server = HttpProvider('https://api.shasta.trongrid.io')

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)
tron.private_key = '8073cb72ca6afb1fd9e0903725e66d2bea215090a8eb7e5a96b78e7db62e7902'
tron.default_address = 'TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL'

print(tron.trx.get_transaction('643db34980dae6effcb95fe73ccb10d0ed010647d7afa34c5c940db351d0652f'))

