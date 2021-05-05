>>> from web3 import Web3
>>> node_provider = 'YOUR_INFURA.IO_NODE_KEY'
>>> web3_connection = Web3(Web3.HTTPProvider(node_provider))
>>> web3_connection.isConnected()
True
>>> w3.eth.getBlock('latest') #Return latest block info
>>> block = w3.eth.getBlock('latest')
>>> block.difficulty #Return latest block difficulty
>>> dir(block) #Return the list of functions that can be applied on "block"
['__abstractmethods__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__orig_bases__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_apply_if_mapping', '_is_protocol', '_repr_pretty_', 'difficulty', 'extraData', 'gasLimit', 'gasUsed', 'get', 'hash', 'items', 'keys', 'logsBloom', 'miner', 'mixHash', 'nonce', 'number', 'parentHash', 'receiptsRoot', 'recursive', 'sha3Uncles', 'size', 'stateRoot', 'timestamp', 'totalDifficulty', 'transactions', 'transactionsRoot', 'uncles', 'values']
>>> block.totalDifficulty
24220580091273119027414
>>> w3.eth.getBalance('YOUR_ETH_PUBLIC_KEY')
496448628000000000
>>> balance = w3.eth.getBalance('YOUR_ETH_PUBLIC_KEY')
>>> w3.fromWei(balance, 'ether') #Return balance in Eth
Decimal('0.496448628')

>>> transaction = w3.eth.getTransaction('YOUR_ETH_PUBLIC_KEY')
>>> transaction
>>> transaction.value
0
>>> transaction.blockNumber
11671122
>>> dir(transaction)
['__abstractmethods__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__orig_bases__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_apply_if_mapping', '_is_protocol', '_repr_pretty_', 'blockHash', 'blockNumber', 'from', 'gas', 'gasPrice', 'get', 'hash', 'input', 'items', 'keys', 'nonce', 'r', 'recursive', 's', 'to', 'transactionIndex', 'type', 'v', 'value', 'values']
>>> transaction.hash
>>> transaction.nonce
0
>>> transaction.gas
115852
>>> w3.fromWei(transaction.gas, 'ether')
Decimal('1.15852E-13')
>>> w3.fromWei(transaction.gas, 'Gwei')
Decimal('0.000115852')

>>> transaction.gasPrice
44000000000
>>> w3.fromWei(transaction.gasPrice, 'Gwei')
Decimal('44')

// Credit: https://www.youtube.com/watch?v=bqrdDrZXNTs&t=328s
