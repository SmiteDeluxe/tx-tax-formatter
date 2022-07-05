from typing import List

from Chain import Chain
from Tx import Tx
from TxGetter import TxGetter


class WalletAPIServiceScan:
    tx_getter: TxGetter

    def __init__(self, tx_getter: TxGetter):
        self.tx_getter = tx_getter

    def formatForWallet(self, wallet: str, chain: Chain):
        txs: List[Tx] = self.tx_getter.getTxs(wallet, chain)
        print([x.__str__() for x in txs])
