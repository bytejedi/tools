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
tron.private_key = '8073cb72ca6afb1fd9e0903725e66d2bea215090a8eb7e5a96b78e7db62e7902'
tron.default_address = 'TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL'


def sign_and_broadcast():
    try:
        create_tx = tron.transaction_builder.trigger_smart_contract(
            owner_address='TRu2DruRJDjVsqno7CwXMzJb7vQTpVaKmL',
            contract_address='41c67bfc2ed582435f41792aacdb89158f80205467',
            function_selector='mint(address,address,uint256)',
            fee_limit=1000000000,
            call_value=0,
            parameters=[
                {'type': 'address', 'value': "2cedcab10b06a5840f3d88508937abf097dc256e"},
                {'type': 'address', 'value': "2cedcab10b06a5840f3d88508937abf097dc256e"},
                {'type': 'uint256', 'value': 10000}
            ]
        )

        offline_sign = tron.trx.sign(create_tx['transaction'])

        res = tron.trx.broadcast(offline_sign)

        if 'result' in res and res['result'] is True:
            print("success", res['txid'])
        else:
            print(res)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    sign_and_broadcast()
