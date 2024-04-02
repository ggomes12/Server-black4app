from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Operação de Combinação
@app.route('/combinação')
def combinação():
    n = int(request.args.get('n'))
    k = int(request.args.get('k'))
    result = math.comb(n, k)
    return jsonify({'result': result})

# Operação de Permutação
@app.route('/permutação')
def permutação():
    n = int(request.args.get('n'))
    result = math.factorial(n)
    return jsonify({'result': result})

# Operação de Arranjo
@app.route('/arranjo')
def arranjo():
    n = int(request.args.get('n'))
    k = int(request.args.get('k'))
    result = math.perm(n, k)
    return jsonify({'result': result})

# Operação de Fatorial
@app.route('/fatorial')
def fatorial():
    n = int(request.args.get('n'))
    result = math.factorial(n)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
    
    
    
