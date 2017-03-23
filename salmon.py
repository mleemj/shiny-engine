from itertools import product

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sales_strategy.html')


@app.route('/_curate')
def max_sales_strategy():
    nc = request.args.get('num_collections', type=int)
    list_combinations = product(range(2), repeat=nc)
    rdict = dict()
    index = 0
    for combination in list_combinations:
        rdict[index] = list(combination)
        index += 1
    return jsonify(rdict)


if __name__ == '__main__':
    app.run()
