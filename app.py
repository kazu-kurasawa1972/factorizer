from flask import Flask, request, jsonify

app = Flask(__name__)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

@app.route('/factorize', methods=['GET'])
def factorize():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"error": "Parameter 'number' is required and must be an integer."}), 400
    if number <= 1:
        return jsonify({"error": "Number must be greater than 1."}), 400

    factors = prime_factors(number)
    return jsonify({
        "number": number,
        "prime_factors": factors
    })

if __name__ == '__main__':
    app.run()
