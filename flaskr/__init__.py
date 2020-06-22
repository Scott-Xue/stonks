from flask import Flask, request, render_template
from src import arbitrage


def create_app(test_config=None):
    # flask server
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=("GET", "POST"))
    def print_opportunities():
        ticker = request.args.get('ticker')
        if ticker:
            q = arbitrage.Query(stock_names=[ticker])
            opportunities = q.find_opportunities()
            return str(opportunities)
        return render_template("base.html")

    return app
