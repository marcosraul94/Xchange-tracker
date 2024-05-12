from flask import Flask, request
from src.enums import Currency
from src.entities.bank import Bank
from src.views.rate import RateView
from src.views.bank import BankView
from src.views.migration import MigrationView
from src.utils.serialization import DateSerialization


app = Flask(__name__)


@app.route("/banks", methods=["GET"])
def banks():
    return BankView().get()


@app.route("/rates", methods=["GET", "POST"])
def rates():
    if request.method == "POST":
        return RateView().post()

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

    return RateView().get(day, currency, bank)


@app.route("/migrations", methods=["GET"])
def migrate():
    return MigrationView().get()
