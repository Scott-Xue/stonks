from flask import Flask, request, render_template, redirect, url_for
from src import arbitrage


def create_app(test_config=None):
    # flask server
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        return render_template("base.html")

    @app.route('/stock/<stock_name>')
    def print_opportunities(stock_name):
        q = arbitrage.Query(stock_names=[stock_name])
        opportunities = q.find_opportunities()
        return str(opportunities)
    return app
