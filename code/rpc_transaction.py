from bitcoin.rpc import RawProxy

p = RawProxy()

# Aya's transaction ID
txid = "d9de82eb8d5a325d84520b949cf55789a88066f355f1501bd0e6626549738f93"

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
    print(output['scriptPubKey']['addresses'], output['value'])
