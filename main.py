from fastapi import FastAPI
import random
from datetime import date 
from fastapi.responses import HTMLResponse
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

kirby = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠿⠛⠛⠛⠛⠛⠛⠛⠿⠷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡾⠟⠛⠛⠛⠿⣦⣄⠀⣠⣴⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡟⠀⠀⠀⠀⠀⠀⠈⢙⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠉⢱⡀⠀⠀⠀⠀⡜⠁⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀
⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡇⠀⠀⠀⢰⡇⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀
⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣶⣿⡇⠀⠀⠀⢸⣿⣶⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀
⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀
⠀⠀⠀⠹⣷⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠁⠀⠀⠀⠀⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡀⠀⠀
⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⢠⣶⣶⣶⣦⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⠀⢈⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀
⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀
⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⣀⣴⡿⠁⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⡛⠛⠉⠀⠀⠀
⠀⠀⠀⢀⣴⣿⠋⠁⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠈⠙⠻⣶⣄⠀⠀⠀
⠀⢀⣴⣿⣯⣴⡆⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⢰⣶⣬⣻⣷⡀⠀
⠀⣾⠏⢸⣿⠿⠃⠀⠀⠀⠀⠀⠙⠳⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠀⠀⠀⠀⠀⠈⠻⢿⡿⠹⣿⡀
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢦⣤⣤⣀⣀⠀⢀⣀⣠⣤⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡇
⠀⠻⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣬⣿⠟⠛⠻⣿⣯⣥⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡿⠃
⠀⠀⠀⠉⠛⠛⠿⠿⠶⠶⠶⠶⠶⠿⠿⠿⠟⠛⠛⠋⠉⠀⠀⠀⠀⠀⠉⠉⠛⠛⠻⠿⠿⠿⠶⠶⠶⠶⠶⠾⠿⠛⠛⠋⠁⠀⠀"""

def días_juntos():
    inicio=date(2024,10,24)
    hoy=date.today()
    días=(hoy-inicio).days
    return días

@app.get("/días")
def endpoint_dias():
    return {"días_juntos": días_juntos()}

@app.get("/", response_class=HTMLResponse)
def inicio():
    parte1 = f"""
    <html>
        <head>
            <style>
                body {{
                    background-color: #ffb7c5;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 40px;
                }}
                pre {{
                    display: inline-block;
                    text-align: left;
                }}
                h1 {{ color: #cc0066; }}
            </style>
        </head>
        <body>
            <h1>¡Hola pequeñita! 💖</h1>
            <p>Este es un servidor que acabo de crear con FastAPI y Python :D</p>
            <p>Llevamos <b>{días_juntos()}</b> días juntos 🐛</p>
            <pre>"""

    parte2 = f"""</pre>
            <p><b>Consejo del día:</b> {random.choice(consejos)}</p>
            <audio controls autoplay loop>
                <source src="https://res.cloudinary.com/dtuuppzl4/video/upload/v1778421028/The_Marcus_Hedges_Trend_Orchestra_-_Song_Of_Storms_SPOTISAVER_1_r3i8yd.mp3" type="audio/mpeg">
            </audio>
            <div style="margin-top: 40px; font-style: italic; color: #cc0066;">
    <p>Hola corazón, espero que leas esto puesto que empezar a escribir estas lineas representan que después de casi 4 horas o 5, no lo sé, terminé. Y pues eso, te amo pero es muy agobiante después de todo, no sé muy bien que decirte, solamente quiero que tengas algo que leer mientras suena la canción. Así que pues eso, te amo y buenas noches. Más tarde me gustaría contarte mis patoaventuras de esta noche, te amo mucho cielo. Buenos días... Esto que estás viendo es un servidor y no tengo palabras para decirte lo divertido y fastidioso que fue; sin embargo, espero sea lindo para ti ver algo así, me imagino que nunca nadie te habia hecho algo así jajaja. Te amo, mucho. Aunque es raro a veces, es lindo estar contigo ocasionalmente.</p>
</div>
        </body>
    </html>"""

    return parte1 + kirby + parte2

@app.get("/consejo")
def consejo_random():
    return {"consejo": random.choice(consejos)}