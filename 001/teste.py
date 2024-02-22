from random import randint


def sortear(numero):
    lista = []
    todos = []
    for c in range(0, numero):
        while len(lista) < 6:
            n = randint(1, 60)
            if n not in lista:
                lista.append(n)
                lista.sort()
        todos.append(lista[:])
        lista.clear()
    for d in range(0, numero):
        jgs = todos[d]
        print(jgs)


numero = int(input('Digite um numero: '))
sortear(numero)


