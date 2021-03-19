import os
import redis

from flask import Flask, make_response, jsonify

app = Flask(__name__)

#cache = redis.Redis(host="localhost", port=6379, password="")
#cache = redis.Redis(host="172.17.0.2", port=6379, password="")
cache = redis.from_url(os.environ.get("REDISTOGO_URL"))

@app.route("/")
def index():
    return make_response(jsonify("Olá Mundo! Python!"), 200)

@app.route("/<int:numero>")
def calculo(numero):
    if numero < 0 or numero > 10000:
        return make_response(jsonify({"status": "Apenas números entre 0 e 100"}), 404)

    if cache.exists(f'{numero}'):
        resultado = int(cache.get(f'{numero}').decode('utf-8'))
    else:
        resultado = fibonacci(numero)            
        cache.mset({numero:resultado})

    return make_response(jsonify(resultado), 200)

def fibonacci(parametro_numero):
    numero_anterior = 0
    numero_posterior = 1
    numero = 0

    for i in range(parametro_numero):
        numero_anterior = numero_posterior
        numero_posterior = numero
        numero = numero_anterior + numero_posterior
    
    print(numero)
    return numero

if __name__ == "__main__":
  app.run(host ='0.0.0.0')