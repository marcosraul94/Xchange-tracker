from src.views.base import View
from src.repositories.bank import BankRepo
from src.utils.serialization import DictSerialization


class BanksView(View):
    repo = BankRepo()

    def get(self):
        banks = self.repo.find_all()

        return self.format_response(
            [DictSerialization.serialize(bank.to_dict()) for bank in banks]
        )
