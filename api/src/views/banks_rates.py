from .base import View
import src.db as db
from src.repositories.base import Repository


class GetBanksRates(View):
    def __init__(self) -> None:
        pass

    def render(self):
        table = Repository.create_table()
        print(table)

        print("I am here", list(db.get_client().tables.all()))

        return self.format_response("Hello world")


class CreateBanksRates(View):
    def __init__(self) -> None:
        pass

    def render():
        pass
