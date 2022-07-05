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


class TxGetterScan(TxGetter):
    def getTxs(self, wallet: str, chain: Chain) -> List[Tx]:
        resp_json: Dict = requests.get(
            chain.api_base_url + "/api?module=account&action=tokentx&address"
                                 "=0x4298272C3Fc13F951D72a2A1dED8123e031BD04b&page=1&offset=1000&startblock=0&endblock=99999999&sort=desc"
                                 "&apikey=H653P3GCTS2KBATSK2HZC9Q5V3JPBPRMHM").json()
        result: Dict = resp_json['result']

        tx_list: List[Tx] = []
        for res_tx in result:
            time: datetime = datetime.datetime.fromtimestamp(int(res_tx['timeStamp']) / 1e3)
            gas = (int(res_tx['gasPrice']) * int(res_tx['gasUsed'])) * 10 ** (-chain.decimals)

            temp_tx: Tx = Tx(time, res_tx['hash'],
                             res_tx['from'], res_tx['to'], int(res_tx['value']) * 10 ** (-int(res_tx['tokenDecimal'])),
                             res_tx['tokenSymbol'], res_tx['tokenName'],
                             gas)
            tx_list.append(temp_tx)

        return tx_list
