import markdown
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import yfinance as yf  # https://algotrading101.com/learn/yfinance-guide/

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    with open('../README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


infoParser = reqparse.RequestParser()
infoParser.add_argument(
    "ticker", type=str, help="Name of the ticker", required=True)

histParser = reqparse.RequestParser()
histParser.add_argument(
    "ticker", type=str, help="Name of the ticker", required=True)
histParser.add_argument(
    "period", type=str, help="Data period to get historical data", required=True)
histParser.add_argument(
    "interval", type=str, help="Data interval to get historical data", required=True)


class FinInfo(Resource):
    def get(self):
        args = infoParser.parse_args()
        ticker = yf.Ticker(args['ticker'])
        try:
            return {"tickerInfo": ticker.info}
        except:
            abort(404, message="ERROR: Invalid ticker!")


class FinHist(Resource):
    def get(self):
        args = histParser.parse_args()
        print(args)
        ticker = yf.Ticker(args['ticker'])
        try:
            hist = ticker.history(
                period=args['period'], interval=args['interval'])
            hist.index = hist.index.strftime("%Y-%m-%d,%H:%M:%S")
            return {"tickerHist": hist.to_dict(orient="split")}
        except:
            abort(404, message="ERROR: Invalid ticker!")


api.add_resource(FinInfo, '/fin/info/')
api.add_resource(FinHist, '/fin/hist/')

if __name__ == '__main__':
    app.run(debug=True)
