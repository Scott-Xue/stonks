from flask import Flask, request, render_template
from src import arbitrage


def create_app(test_config=None):
    # flask server
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=("GET", "POST"))
    def hello_world():
        if request.method == "POST":
            ticker = request.form["ticker"]
            if ticker:
                q = arbitrage.Query(stock_names=ticker)
                opportunities = q.find_opportunities()
                return str(opportunities)
            else:
                return "Enter a query"
        return render_template("base.html")
    return app
