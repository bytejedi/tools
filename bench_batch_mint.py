#!/user/bin/ven python
# coding=utf-8
import concurrent.futures
import time
from multiprocessing import Pool
from tronapi import Tron
from tronapi import HttpProvider
import gen_address as address

full_node = HttpProvider('https://api.shasta.trongrid.io')
solidity_node = HttpProvider('https://api.shasta.trongrid.io')
event_server = HttpProvider('https://api.shasta.trongrid.io')

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)
tron.private_key = '8073cb72ca6afb1fd9e0903725e66d2bea215090a8eb7e5a96b78e7db62e7902'
tron.default_address = 'TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL'
contract_address = '4181f7e0f75501194bb82e55a896afb6e802ebd42e'
address_count = 100
addr = '0xaEb759C19724572e31D4bc8F7D9d5F3161b056ca'

addresses_str = address.gen_addresses(address_count, addr)
addresses_str = addresses_str.lstrip('["')
addresses_str = addresses_str.rstrip('"]')
addresses = list(addresses_str.split('","'))

max_process = 12
threads_per_process = 12
txs_per_process = 100


def batch_mint_one():
    try:
        create_tx = tron.transaction_builder.trigger_smart_contract(
            owner_address='TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL',
            contract_address=contract_address,
            function_selector='batchMint(address[],address[],uint256,uint256)',
            fee_limit=1000000000,
            call_value=0,
            parameters=[
                {'type': 'address[]', 'value': addresses},
                {'type': 'address[]', 'value': addresses},
                {'type': 'uint256', 'value': 10000},
                {'type': 'uint256', 'value': address_count}
            ]
        )

        # print(create_tx)

        offline_sign = tron.trx.sign(create_tx['transaction'])

        res = tron.trx.broadcast(offline_sign)

        if 'result' in res and res['result'] is True:
            print("success", res['txid'])
        else:
            print(res)

        res = tron.trx.broadcast(offline_sign)

        if 'result' in res and res['result'] is True:
            print("success", res['txid'])
        else:
            print(res)
    except Exception as e:
        print(e)


def sign_and_broadcast_all(process_id):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_per_process) as executor:
        futures = [executor.submit(batch_mint_one) for _ in range(1, txs_per_process + 1)]
        for _ in concurrent.futures.as_completed(futures):
            pass
    print("process_id ", process_id, txs_per_process, " Txs,", threads_per_process,
          "Thread pool execution in " + str(time.time() - start), "seconds")


if __name__ == "__main__":
    start_time = time.time()
    print('start at', str(start_time))
    with Pool(max_process) as p:
        p.map(sign_and_broadcast_all, range(max_process))
    print("==========", txs_per_process * max_process, " Txs,", max_process,
          "Process pool execution in " + str(time.time() - start_time), "seconds")

