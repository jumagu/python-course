import json

planetas = {
    "mercurio": {
        "distancia_sol_km": 57910000,
        "diametro_km": 4879,
        "lunas": 0,
        "tipo": "rocoso",
        "temperatura_promedio_c": 167,
        "periodo_orbital_dias": 88,
    },
    "venus": {
        "distancia_sol_km": 108200000,
        "diametro_km": 12104,
        "lunas": 0,
        "tipo": "rocoso",
        "temperatura_promedio_c": 464,
        "periodo_orbital_dias": 225,
    },
    "tierra": {
        "distancia_sol_km": 149600000,
        "diametro_km": 12756,
        "lunas": 1,
        "tipo": "rocoso",
        "temperatura_promedio_c": 15,
        "periodo_orbital_dias": 365,
    },
    "marte": {
        "distancia_sol_km": 227900000,
        "diametro_km": 6792,
        "lunas": 2,
        "tipo": "rocoso",
        "temperatura_promedio_c": -65,
        "periodo_orbital_dias": 687,
    },
    "jupiter": {
        "distancia_sol_km": 778500000,
        "diametro_km": 142984,
        "lunas": 95,
        "tipo": "gigante gaseoso",
        "temperatura_promedio_c": -110,
        "periodo_orbital_dias": 4333,
    },
    "saturno": {
        "distancia_sol_km": 1432000000,
        "diametro_km": 120536,
        "lunas": 146,
        "tipo": "gigante gaseoso",
        "temperatura_promedio_c": -140,
        "periodo_orbital_dias": 10759,
    },
}

with open("test_files/planets.json", "w") as my_file:
    json.dump(planetas, my_file, indent=4)

with open("test_files/planets.json", "r") as my_file:
    data_read = json.load(my_file)
    print(data_read)
