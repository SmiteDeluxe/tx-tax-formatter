class Chain:
    chain: str
    api_base_url: str
    currency: str
    decimals: int

    def __init__(self, chain: str, api_base_url: str, currency: str, decimals: int):
        self.chain = chain
        self.api_base_url = api_base_url
        self.currency = currency
        self.decimals = decimals
