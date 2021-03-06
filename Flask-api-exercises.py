import flask
import json
import traceback
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
    ]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello World</h1>'''

@app.route('/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    if(results):
        pass
    else:
        results = "No books found"

    return jsonify(results)

#Adding two numbers
@app.route('/adder', methods=['POST'])
def adder():
    result = {}
    try:
        n1 = int(request.form['num_1'])
        n2 = int(request.form['num_2'])
        result['status'] = 1
        result['total'] = n1 + n2
        res = json.dumps(result)
        return res
    except Exception as e :
        print(traceback.format_exc())
        result['status'] = -99
        result['errorName'] = type(e).__name__
        result['errMsg'] = str(e)
        res = json.dumps(result)
        return str(res)

@app.route('/square/<int:number>', methods=["GET"])
def variable_int(number):
    return "Square value is " + str(number * number)

@app.route('/square/<string:name>', methods=['GET'])
def variable_string(name):
    return "Your name is " + str(name)
    
#Reversing string
@app.route('/string-reverse', methods=['POST'])
def reverse():
    result = {}
    try:
        string = str(request.form['str'])
        result['status'] = 1
        result['reversedStr'] = string[::-1]
        res = json.dumps(result)
        return str(res)
    except Exception as e:
        print(traceback.format_exc())
        result['status'] = -99
        result['errMsg'] = str(e).__name__
        res = json.dumps(result)
        return str(res)

@app.route('/stripe/customer', methods=['GET', 'POST', 'DELETE'])
def stripe_customer():
    result = dict()
    if request.method == "GET":
        try:
            customer_id = request.form["customer_id"]
            result["data"] = sunshinelib.get_customer(customer_id)
            result["status"] = 200
        except Exception as e:
            result["status"] = 400
            result['errName'] = type(e).__name__
            result['errMsg'] = str(e)
        return jsonify(result) 
    elif request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            result["data"] = sunshinelib.create_customer(name, email)
            result["status"] = 200
        except Exception as e:
            result["status"] = 400
            result['errName'] = type(e).__name__
            result['errMsg'] = str(e)
        return jsonify(result)
    elif request.method == "DELETE":
        try:
            customer_id = request.form["customer_id"]
            result["data"] = sunshinelib.remove_customer(customer_id)
            result["status"] = 200
        except Exception as e:
            result["status"] = 400
            result['errName'] = type(e).__name__
            result['errMsg'] = str(e)
        return jsonify(result)
    
#Bubble sort
@app.route('/bubble-sort', methods=['POST'])
def bubbleSort():
    result = {}
    try:
        list = str(request.form['str'])
        result['status'] = 1
        arr = []
        for x in list.split(','):
            arr.append(int(x))
        l = len(arr)
        for i in range(l-1):
            for j in range(l-i-1):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        result['sorted'] = arr
        res = json.dumps(result)
        return res
    except Exception as e:
        print(traceback.format_exc())
        result['status'] = -99
        result['errMsg'] = str(e).__name__
        res = json.dumps(result)
        return str(res)


app.run()
