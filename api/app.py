from flask import Flask, request
from src.views.banks_rates import CreateBanksRates, GetBanksRates

app = Flask(__name__)


@app.route("/banks_rates", methods=["GET", "POST"])
def banks_rates():
    if request.method == "POST":
        return CreateBanksRates().render()

    return GetBanksRates().render()
