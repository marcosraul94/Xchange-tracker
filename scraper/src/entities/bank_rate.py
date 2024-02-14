class BankRate:
    def __init__(self, bank_id: str, buy: float, sell: float) -> None:
        self.bank_id = bank_id
        self.buy = buy
        self.sell = sell


class DollarRate(BankRate):
    pass


class EuroRate(BankRate):
    pass
