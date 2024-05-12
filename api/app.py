from decimal import Decimal
from flask import Flask, request
from src.enums import Currency
from src.entities.bank import Bank
from src.views.rates import RatesView
from src.views.banks import BanksView
from src.views.migrations import MigrationsView
from src.utils.serialization import DateSerialization


app = Flask(__name__)


@app.route("/banks", methods=["GET"])
def banks():
    return BanksView().get()


@app.route("/rates", methods=["GET", "POST"])
def rates():
    if request.method == "POST":
        rates = [
            {
                "bank_name": rate["bank_name"],
                "amount": Decimal(rate["amount"]),
                "currency": Currency(rate["currency"]),
            }
            for rate in request.json['rates']
        ]

        return RatesView().post(rates)

    day = (
        DateSerialization.deserialize(request.args.get("day"))
        if request.args.get("day")
        else None
    )
    currency = Currency(request.args.get("currency"))
    bank = (
        Bank(request.args.get("bank_name"))
        if request.args.get("bank_name")
        else None
    )

    return RatesView().get(day, currency, bank)


@app.route("/migrations", methods=["GET"])
def migrate():
    return MigrationsView().get()
