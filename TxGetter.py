from abc import ABC, abstractmethod
from typing import List
import requests
from typing import Dict
from Chain import Chain
from Tx import Tx
import datetime


class TxGetter(ABC):
    @abstractmethod
    def getTxs(self, wallet: str, chain: Chain):
        pass


def genNormalTx(res_tx: Dict, chain: Chain) -> Tx:
    time: datetime = datetime.datetime.fromtimestamp(int(res_tx['timeStamp']) / 1e3)
    gas = (int(res_tx['gasPrice']) * int(res_tx['gasUsed'])) * 10 ** (-chain.decimals)

    temp_tx: Tx = Tx(time, res_tx['hash'],
                     res_tx['from'], res_tx['to'], int(res_tx['value']) * 10 ** (-int(chain.decimals)),
                     chain.currency, chain.currency,
                     gas)
    return temp_tx


def genTokenTransferTx(res_tx: Dict, chain: Chain) -> Tx:
    time: datetime = datetime.datetime.fromtimestamp(int(res_tx['timeStamp']) / 1e3)
    gas = (int(res_tx['gasPrice']) * int(res_tx['gasUsed'])) * 10 ** (-chain.decimals)

    temp_tx: Tx = Tx(time, res_tx['hash'],
                     res_tx['from'], res_tx['to'], int(res_tx['value']) * 10 ** (-int(res_tx['tokenDecimal'])),
                     res_tx['tokenSymbol'], res_tx['tokenName'],
                     gas)
    return temp_tx


class TxGetterScan(TxGetter):

    def getTxs(self, wallet: str, chain: Chain) -> List[Tx]:

        # Gets all token transfers not involving the chain token except gas, can include same hash multiple times
        resp_json: Dict = requests.get(
            chain.api_base_url + "/api?module=account&action=tokentx&address=" + wallet +
            "&page=1&offset=10000&startblock=0"
            "&endblock=99999999&sort=desc "
            "&apikey=" + chain.api_key).json()
        result: Dict = resp_json['result']

        tx_list: List[Tx] = []
        for res_tx in result:
            tx_list.append(genTokenTransferTx(res_tx, chain))

        # Gets all normal transactions and only uses not already
        # included hashes and non 0 value ones for already included ones (means chain token transfer)
        resp_json: Dict = requests.get(
            chain.api_base_url + "/api?module=account&action=txlist&address=" + wallet +
            "&startblock=0&endblock=99999999&page=1"
            "&offset=10000&sort=desc&apikey=" + chain.api_key).json()
        result: Dict = resp_json['result']

        for res_tx in result:
            if res_tx['value'] != "0":
                # Means Matic was involved
                tx_list.append(genNormalTx(res_tx, chain))

            elif not any(x.tx_hash == res_tx['hash'] for x in tx_list):
                # Means it was a tx only involving gas
                tx_list.append(genNormalTx(res_tx, chain))

        return tx_list
