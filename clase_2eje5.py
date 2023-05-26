#Cristofori Magali

heroes_info = [
{
    "nombre": "super girl",
    "ID":1,
    "Origen": "kripton",
    "Habilidades": ["volar", "fuerza", "velocidad", "volar", "fuerza", "velocidad"],
    "identidad": "Kar zor-el"

    
},
{
    "nombre": "sharman",
    "ID":25,
    "Origen": "tierra",
    "Habilidades": ["volar", "fuerza", "velocidad", "magia", "fuerza", "velocidad"],
    "identidad": "Billy Batson"

    
},
{
    "nombre": "power girl",
    "ID":14,
    "Origen": "kripton",
    "Habilidades": ["volar", "fuerza", "congelar", "congelar"],
    "identidad": "Karen starr"

    
},
{
    "nombre": "wonder woman",
    "ID":29,
    "Origen": "amazonia",
    "Habilidades": ["agilidad", "fuerza", "lazo de la verdad", "escudo"],
    "identidad": "Diana prince"

    
}
]

for i in heroes_info:
    nombre = i ["nombre"] 
    id = i ["ID"]
    origen = i ["Origen"] 
    habilidades =set(i ["Habilidades"])  
    identidad = i ["identidad"]

    habilidades_pipe = " | ".join(habilidades)

    print(f"""
        nombre:{nombre}, \t
        id:{id}, \t
        origen:{origen}, \t
        habilidades:{habilidades_pipe}, \t
        identidad{identidad}
        ------------------------------------""")
    


    
