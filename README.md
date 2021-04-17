# TSP-Routy

#### Esta api se encuentra desplegada en el siguiente link de heroku:
* https://tsp-routy.herokuapp.com/

Esta es una api simple creada en flask que usa 
una libreria llamada tsp_solver2 para calcular la ruta más corta,
usa como datos de entrada las coordenadas dadas por la app de flutter
routy y en el proceso llama a la api de Matrix de OpenRouteService para
obtener una matrix de distancia, esta matrix se pasa como parametro 
a una funcion de la libreria de tsp_solver2 y esta libreria calcula usando
el algoritmo de greedy la ruta más corta.
La api tiene una salida como la siguiente:
* {

    "caminoMinimo": [
    
        [
            9.70093,
            48.477473
        ],
        [
            9.207916,
            49.153868
        ],
        [
            37.573242,
            55.801281
        ],
        [
            115.663757,
            38.106467
        ],
        [
            9.70093,
            48.477473
        ]
    ],
    
    "distanciaMinima": 20307864.03,
    
    "distancias": {
    
        "distancias": [
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
        "message": "Estas son las distancias dadas por la api ORS"
    },
    
    "message": "este es el camino más corto",
    
    "orden": [
    
        0,
        1,
        2,
        3,
        0
    ]
}