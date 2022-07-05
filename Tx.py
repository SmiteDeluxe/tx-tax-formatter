from typing import List
from datetime import datetime


#
#
# class logparam:
#     name: str
#     type: str
#     indexed: bool
#     decoded: bool
#     value: str
#
#     def __init__(self, name: str,
#                  type: str,
#                  indexed: bool,
#                  decoded: bool,
#                  value: str):
#         self.name = name
#         self.type = type
#         self.indexed = indexed
#         self.decoded = decoded
#         self.value = value
#
#
# class decodedlog:
#     name: str
#     signature: str
#     params: list[logparam]
#
#     def __init__(self, name: str, signature: str, params: list[logparam]):
#         self.name = name
#         self.signature = signature
#         self.params = params
#
#
# class logevent:
#     block_signed_at: str
#     block_height: int
#     tx_offset: int
#     log_offset: int
#     tx_hash: str
#     raw_log_topics: list[str]
#     sender_contract_decimals: int
#     sender_name: str
#     sender_contract_ticker_symbol: str
#     sender_address: str
#     sender_address_label: str
#     sender_logo_url: str
#     raw_log_data: str
#     decoded: list[decodedlog]
#
#     def __init__(self, block_signed_at: str,
#                  block_height: int,
#                  tx_offset: int,
#                  log_offset: int,
#                  tx_hash: str,
#                  raw_log_topics: list[str],
#                  sender_contract_decimals: int,
#                  sender_name: str,
#                  sender_contract_ticker_symbol: str,
#                  sender_address: str,
#                  sender_address_label: str,
#                  sender_logo_url: str, raw_log_data: str,
#                  decoded: list[decodedlog]):
#         self.block_signed_at = block_signed_at
#         self.block_height = block_height
#         self.tx_offset = tx_offset
#         self.log_offset = log_offset
#         self.tx_hash = tx_hash
#         self.raw_log_topics = raw_log_topics
#         self.sender_contract_decimals = sender_contract_decimals
#         self.sender_name = sender_name
#         self.sender_contract_ticker_symbol = sender_contract_ticker_symbol
#         self.sender_address = sender_address
#         self.sender_address_label = sender_address_label
#         self.sender_logo_url = sender_logo_url
#         self.raw_log_data = raw_log_data
#         self.decoded = decoded
#
#
# class tx:
#     block_signed_at: str
#     block_height: int
#     tx_hash: str
#     tx_offset: int
#     successful: bool
#     from_address: str
#     from_address_label: str
#     to_address: str
#     to_address_label: str
#     value: int
#     value_quote: float
#     gas_offered: int
#     gas_spent: int
#     gas_price: int
#     fees_paid: int
#     gas_quote: float
#     gas_quote_rate: float
#     log_events: list[logevent]
#
#     def __init__(self, block_signed_at: str, block_height: int, tx_hash: str, tx_offset: int, successful: bool,
#                  from_address: str, from_address_label: str, to_address: str, to_address_label: str, value: int,
#                  value_quote: float, gas_offered: int, gas_spent: int, gas_price: int, fees_paid: int, gas_quote: float,
#                  gas_quote_rate: float, log_events: list[logevent]):
#         self.block_signed_at = block_signed_at
#         self.block_height = block_height
#         self.tx_hash = tx_hash
#         self.tx_offset = tx_offset
#         self.successful = successful
#         self.from_address = from_address
#         self.from_address_label = from_address_label
#         self.to_address = to_address
#         self.to_address_label = to_address_label
#         self.value = value
#         self.value_quote = value_quote
#         self.gas_offered = gas_offered
#         self.gas_spent = gas_spent
#         self.gas_price = gas_price
#         self.fees_paid = fees_paid
#         self.gas_quote = gas_quote
#         self.gas_quote_rate = gas_quote_rate
#         self.log_events = log_events
#
#
# class chainresp:
#     address: str
#     updated_at: str
#     next_update_at: str
#     quote_currency: str
#     chain_id: int
#     items: list[tx]

class Tx:
    time_stamp: datetime
    tx_hash: str
    from_addr: str
    to_addr: str
    value: float
    token_symbol: str
    token_name: str
    gas_fee: float

    def __init__(self, time_stamp: datetime,
                 tx_hash: str,
                 from_addr: str,
                 to_addr: str,
                 value: float,
                 token_symbol: str,
                 token_name: str,
                 gas_fee: float):
        self.time_stamp = time_stamp
        self.tx_hash = tx_hash
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.value = value
        self.token_symbol = token_symbol
        self.token_name = token_name
        self.gas_fee = gas_fee

    def __str__(self):
        return "Hash: " + self.tx_hash + " / Time: " + self.time_stamp.isoformat() + " / From: " + self.from_addr + " / To: " + self.to_addr + " / Value: " + str(
            self.value) + " / Token: " + self.token_symbol + " / Gas: " + str(self.gas_fee)
