from flask import Flask, render_template, request, jsonify, Response, \
    stream_with_context

from Max_Sales_Strategy import MaxSalesStrategy

from itertools import product

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/_add_numbers')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('max_sales_strategy.html')

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

# maxSales = MaxSalesStrategy(num_of_collections)
# list_combinations = maxSales.get_list_combinations()
# return Response(stream_template('max_sales_strategy.html',
#                                 combinations_list=list_combinations))


@stream_with_context
def stream_template(template_name, **context):
    app.update_template_context(context)
    template = app.jinja_env.get_template(template_name)
    templateStream = template.stream(context)
    templateStream.enable_buffering(5)
    return templateStream


if __name__ == '__main__':
    app.run()
