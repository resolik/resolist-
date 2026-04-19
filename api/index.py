import os
from flask import Flask, render_template

# Находим путь к текущей папке (api)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Авто-поиск папок: проверяем внутри api и на уровень выше
template_dir = os.path.join(base_dir, 'templates')
if not os.path.exists(template_dir):
    template_dir = os.path.join(base_dir, '..', 'templates')

static_dir = os.path.join(base_dir, 'static')
if not os.path.exists(static_dir):
    static_dir = os.path.join(base_dir, '..', 'static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

demons = [
    {"name": "Thinking Space 2", "img": "thinking_space_2.jpg", "link": "https://youtu.be/CELNmHwln_c?si=L2DfYlm0zWgLt_Nh"},
    {"name": "Flamewall", "img": "flamewall.jpg", "link": "https://youtu.be/x4Io4zkWVRw?si=tTjv7PfTzc4maUEQ"},
    {"name": "Amethyst", "img": "amethyst.jpg", "link": "https://youtu.be/4lfkzz1VCbA?si=dlboDpOFJkODERqP"},
    {"name": "Tidal Wave", "img": "tidal_wave.jpg", "link": "https://youtu.be/9fsZ014qB3s?si=ZNXSZV2nVGu775sV"},
    {"name": "Orbit", "img": "orbit.jpg", "link": "https://youtu.be/QKcv8DkNPd0?si=lwAqzEnSq4ny34EQ"},
    {"name": "Nullskapes", "img": "nullskapes.jpg", "link": "https://youtu.be/EztneTPp5CU?si=rUVAw8jruH5v0Aeg"},
    {"name": "Boobawamba", "img": "boobawamba.jpg", "link": "https://youtu.be/example7"},
    {"name": "Quantuesue Processing", "img": "qp.jpg", "link": "https://youtu.be/example8"},
    {"name": "Every End", "img": "every_end.jpg", "link": "https://youtu.be/example9"},
    {"name": "Sumsuming Vortrex", "img": "sv.jpg", "link": "https://youtu.be/example10"},
    {"name": "Andromeda", "img": "andromeda.jpg", "link": "https://youtu.be/example11"},
    {"name": "Anathema", "img": "anathema.jpg", "link": "https://youtu.be/example12"},
    {"name": "Silent Clubstep", "img": "sc.jpg", "link": "https://youtu.be/example13"},
    {"name": "Ashley Wave Trials", "img": "awt.jpg", "link": "https://youtu.be/example14"},
    {"name": "Avernus", "img": "avernus.jpg", "link": "https://youtu.be/example15"},
    {"name": "Acheron", "img": "acheron.jpg", "link": "https://youtu.be/example16"},
    {"name": "Spectre", "img": "spectre.jpg", "link": "https://youtu.be/example17"},
    {"name": "Menace", "img": "menace.jpg", "link": "https://youtu.be/example18"},
    {"name": "Abyss of Darkness", "img": "aod.jpg", "link": "https://youtu.be/example19"},
    {"name": "Defeated Circles", "img": "dc.jpg", "link": "https://youtu.be/example20"}
]

@app.route('/')
def home():
    return render_template('index.html', list_of_demons=demons)
            
