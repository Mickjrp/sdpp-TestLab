from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "index!"

@app.route('/plus/<a>/<b>', methods=['GET'])
def plus(a,b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return jsonify({'message': 'Invalid input'}), 400
    return jsonify({'resule':a+b}), 200

@app.route('/is_prime/<num>', methods=['GET'])
def checkPrime(num):
    try:
        num = int(num)
    except ValueError:
        return jsonify({'message': 'Invalid input'}), 400
    
    def isPrime(n):
        if n<1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                return False
        return True
    result = isPrime(num)
    return jsonify(result), 200
    
@app.route('/is_odd_or_even/<num>', methods = ['GET'])
def checkResult(num):
    try:
        num = int(num)
    except ValueError:
        return jsonify({'message' : 'Invalid Input'}), 400
    
    if num%2 != 0:
        return jsonify({num : 'is Odd'}), 200
    elif num%2 == 0:
        return jsonify({num : 'is Even'}), 200
        


if(__name__) == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)