class Chain:
    chain: str
    api_base_url: str
    currency: str
    decimals: int
    api_key: str

    def __init__(self, chain: str, api_base_url: str, currency: str, decimals: int, api_key: str):
        self.chain = chain
        self.api_base_url = api_base_url
        self.currency = currency
        self.decimals = decimals
        self.api_key = api_key
