#!/user/bin/ven python
# coding=utf-8
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


def batch_mint_one():
    try:
        addresses_str = address.gen_addresses(address_count, addr)
        addresses_str = addresses_str.lstrip('["')
        addresses_str = addresses_str.rstrip('"]')
        addresses = list(addresses_str.split('","'))
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


if __name__ == "__main__":
    batch_mint_one()
