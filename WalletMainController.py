import json
from Chain import Chain
from WalletAPIService import WalletAPIServiceScan
from TxGetter import TxGetterScan

if __name__ == '__main__':
    wallet_api_service_scan = WalletAPIServiceScan(TxGetterScan())
    chains = open('ChainData.json')
    chains_data = json.load(chains)
    to_analyse = open('ToAnalyse.json')
    to_analyse_data = json.load(to_analyse)

    for wallet in to_analyse_data['wallets']:
        needed_chain_data = next((x for x in chains_data['chains'] if x['chain'] == wallet['chain']), None)
        wallet_add = wallet['addr']

        if needed_chain_data is None:
            raise Exception("Chain " + wallet['chain'] + " not found in ChainData.json")

        chain_obj = Chain(needed_chain_data['chain'], needed_chain_data['api_base_url'], needed_chain_data['currency'],
                          needed_chain_data['decimals'], needed_chain_data['api_key'])

        wallet_api_service_scan.formatForWallet(wallet_add, chain_obj)
