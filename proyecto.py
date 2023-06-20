import random
lista_palabras = ["marioneta", "helicoptero", "pintoresco", "radiador","marmota"]
intentos = 6
aciertos = 0
letras_correctas = []
letras_erroneas = []
juego_terminado = False


def mezclar(lista):
    eleccion = random.choice(lista)
    return eleccion

def guiones():
    resultado = []
    for letra in palabra:
        if letra in letras_correctas and letra not in letras_erroneas:
            resultado.append(letra)
        else:
            resultado.append("-")
    print(resultado)




def pedir_letra():
    letra_elegida = input("Elige una letra: ")

    while letra_elegida not in ("abcdefghijklmnopqrstuvwxyz"):
        letra_elegida = input("Elige una letra: ")
    if letra_elegida in palabra:
        letras_correctas.append(letra_elegida)
        return
    elif letra_elegida in letras_correctas:
        print("Letra ya usada. ")
    else:
        letras_erroneas.append(letra_elegida)
        letras_correctas.append(letra_elegida)
        intentos =-1
        return
def chequear_palabra():
    contador = 0
    for letra in palabra:
        if letra in letras_correctas:
            contador+= 1
    if contador == len(palabra):
        return True
    else:
        return False

def ganar():
    print(f"Has adivinado la palabra. ")
def game_over():
    print(f"Se ha acabado el juego, la palabra era {palabra}")

palabra = mezclar(lista_palabras)

while intentos > 0:
    guiones()
    pedir_letra()
    if chequear_palabra():
        ganar()
        break

game_over()



