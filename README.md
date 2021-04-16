# TSP-Routy

Esta es una api simple creada en flask que usa 
una libreria llamada tsp_solver2 para calcular la ruta más corta,
usa como datos de entrada las coordenadas dadas por la app de flutter
routy y en el proceso llama a la api de Matrix de OpenRouteService para
obtener una matrix de distancia, esta matrix se pasa como parametro 
a una funcion de la libreria de tsp_solver2 y esta libreria calcula usando
el algoritmo de greedy la ruta más corta.
La api tiene una salida como la siguiente:
{
    "CaminoMinimo": [
        0,
        1,
        2,
        3,
        0
    ],
    "Distancias": [
        [
            0.0,
            140854.61,
            2434699.25,
            9962183.0
        ],
        [
            139772.78,
            0.0,
            2386175.5,
            9913659.0
        ],
        [
            2381593.75,
            2333649.25,
            0.0,
            7550648.0
        ],
        [
            10106755.0,
            10058810.0,
            7727687.0,
            0.0
        ]
    ],
    "distanciaMinima": 20307864.03,
    "message": "este es el camino más corto"
}