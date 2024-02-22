from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)
todos = {}


@app.route('/')
def homepage():
    return render_template('homepage.html')


def sortear(numero):
    lista = []

    for c in range(0, numero):
        while len(lista) < 6:
            n = randint(1, 60)
            if n not in lista:
                lista.append(n)
                lista.sort()
        todos[f'Jogo {c + 1}: '] = lista[:]
        lista.clear()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        sortear(numero)
        return render_template('homepage.html', todos=todos.items())
    return render_template('homepage.html', todos=[])


if __name__ == "__main__":
    app.run(debug=True)
