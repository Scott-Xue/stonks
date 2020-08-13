from flask import Flask, render_template, jsonify
from flask_cors import CORS
from src import arbitrage


def create_app(test_config=None):
    # flask server
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/')
    def index():
        return render_template("base.html")

    @app.route('/stock/<stock_name>')
    def print_opportunities(stock_name):
        q = arbitrage.Query(stock_names=[stock_name])
        res = {}
        opportunities = q.find_opportunities()
        for opportunity in opportunities:
            name, ops = opportunity
            expiry_dict = dict(ops)
            res[name] = expiry_dict
        return jsonify(res)
    return app
