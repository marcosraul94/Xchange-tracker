from src.entities.bank import Bank
from src.repositories.bank import BankRepo


def migrate():
    bank_names = [
        "Popular",
        "Banreservas",
        "Scotiabank",
        "BHD",
        "APAP",
        "BANESCO",
        "PROMERICA",
    ]
    banks = [Bank(bank_name) for bank_name in bank_names]

    BankRepo().create_all(banks)
