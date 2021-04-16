from flask import Flask, jsonify, request
from tsp_solver.greedy import solve_tsp
from tsp_solver.util import path_cost
import requests

app = Flask(__name__)

@app.route('/calcularRuta', methods=['POST'])
def calcularRuta():

    headers = request.headers
    apiKey = headers['x-api-key']
    body = request.get_json()
    myheaders = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': apiKey,
        'Content-Type': 'application/json; charset=utf-8'
    }
    call = requests.post('https://api.openrouteservice.org/v2/matrix/driving-car', json=body, headers=myheaders)
    print(call.status_code)
    if (call.status_code==200):
        jsonResponse = call.json()
        distances = jsonResponse['distances']
        path = solve_tsp(distances, endpoints=(0, 0)) #halla el camino más corto iniciando en 0 y terminando en 0
        distance = path_cost(distances, path)       #calcula la distancia del camino mas corto
        ordenado = []
        for i in path:
            ordenado.append(body['locations'][i])
        return jsonify({
                    'orden': path,
                    'caminoMinimo': ordenado,
                    'distanciaMinima': distance,
                    'message': 'este es el camino más corto',
                    'distancias': {'distancias':distances, 'message': 'Estas son las distancias dadas por la api ORS'}}), 200
    else:
        return jsonify({'message': 'error en el llamado a la api de ors'}), 400


@app.route('/', methods=['GET'])
def home():
    return jsonify({'Message': 'La app esta funcionando, ve a la ruta calcularRuta tipo POST para su funcionalidad'})

if __name__ == '__main__':
    app.run(debug=True)
