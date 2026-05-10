from fastapi import FastAPI
import random
from datetime import date 
app = FastAPI()

consejos = [
    "No te precipites por tu examen, eres una mujer espectacular y no hay nada que temer, mucho menos con un simple examen",
    "Recuerda que las vaquitas son muy inteligentes y no hay cosa que no puedan lograr",
    "Recuerda que las estrellas nacieron de la incertidumbre, así que no te desesperes por el caos que hay actualmente, con el tiempo vas a brillar más que cualquier punto del lindo firmamento que tanto grita tu nombre en las noches",
    "Te faltan 10, 20, 30, ¿40 días? no lo sé, pero no es importante, mi conejita hermosa va a pasarlo sin importar si lo presenta mañana, en una semana o en dos. Confío en ti más que en mí mismo, te amo",
    "Oruguita bella, te estás esforzando y eso definitivamente lo vas a notar pronto, te amo.",
    "Tengo muchas ganas de construir una vida contigo, de hacer miles de cosas, no tengas miedo de equivocarte hoy, independientemente de lo que pase vamos a estar juntos y construiremos algo muy lindo para los dos",
    "Si te sientes mal o sobrepasada recuerda que siempre podrás vivir de hacer pastelitos y hacer a la gente feliz ^^, como a mí",
    "Inteligente, talentosa, hermosa, dulce, amable, divertida, creativa, interesante, única, especial, increíble, maravillosa, ¿qué más puedo decirte? eres la mejor persona que he conocido y no hay nada que no puedas lograr, te amo con todo mi corazón",
    "🐛💖🐙💖",
    "Te amo princesa, espero que hayas descansado. Recuerda que eres lo más importante en el mundo de tu novio",
]


def días_juntos():
    inicio=date(2024,10,24)
    hoy=date.today()
    días=(hoy-inicio).days
    return días

@app.get("/días")
def endpoint_dias():
    return {"días_juntos": días_juntos()}

@app.get("/")
def inicio():
    return {
        "mensaje": "¡Hola cielo! este es un servidor que acabo de crear con FastAPI y Python :D.",
        "añadido": "También quería recortarte los días que llevamos juntos, que son minusculos en comparación a lo que hemos pasado, pero igual sirven para poder señalar ese bonito día que nos conocimos <3",
        "días_juntos": días_juntos(),
        "consejo": random.choice(consejos)
    }

@app.get("/consejo")
def consejo_random():
    return {"consejo": random.choice(consejos)}