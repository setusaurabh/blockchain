from bitcoin.rpc import RawProxy

p = RawProxy()

# The height of the block
blockheight = 300000

blockhash = p.getblockhash(blockheight)

block = p.getblock(blockhash)

transactions = block['tx']

block_value = 0
count =0

# Iterate through each transaction ID in the block
for txid in transactions:
    tx_value = 0
    count = count + 1 
    # Retrieve the raw transaction by ID
    raw_tx = p.getrawtransaction(txid)
    # Decode the transaction
    decoded_tx = p.decoderawtransaction(raw_tx)
    # Iterate through each output in the transaction
    for output in decoded_tx['vout']:
        # Add up the value of each output
        tx_value = tx_value + output['value']
        
    # Add the value of this transaction to the total 
    block_value = block_value + tx_value
    average_count = block_value/count
print("Average size of transaction: ", average_count)