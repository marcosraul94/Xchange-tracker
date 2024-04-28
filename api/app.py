from flask import Flask, request
from src.views.rates import CreateRates, GetRates

app = Flask(__name__)


@app.route("/rates", methods=["GET", "POST"])
def rates():
    if request.method == "POST":
        return CreateRates().render()

    return GetRates().render()
