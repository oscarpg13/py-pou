import random

def minmax(value):
    return max(0, min(value, 100))

def iniciar(nombre):
    return {
        'Nombre': nombre,
        'Edad': 0,
        'Hambre': random.randint(0, 50),
        'Energia': random.randint(50, 100),
        'Felicidad': random.randint(50, 100),
        'Salud': 100,
        'Estado': True
    }

def estado(pou):
    print("Nombre:", pou['Nombre'])
    print("Edad:", pou['Edad'])
    print("Hambre:", pou['Hambre'])
    print("Energia:", pou['Energia'])
    print("Felicidad:", pou['Felicidad'])
    print("Salud:", pou['Salud'])

def jugar(pou):
    pou['Hambre'] = minmax(pou['Hambre'] + random.randint(5, 10))
    pou['Energia'] = minmax(pou['Energia'] - random.randint(10, 20))
    pou['Felicidad'] = minmax(pou['Felicidad'] + random.randint(5, 10))
    pou['Salud'] = minmax(pou['Salud'] - random.randint(5, 15))
    pou['Edad'] += 1

def dormir(pou):
    pou['Hambre'] = minmax(pou['Hambre'] + random.randint(5, 10))
    pou['Energia'] = minmax(pou['Energia'] + random.randint(10, 20))
    pou['Felicidad'] = minmax(pou['Felicidad'] - random.randint(5, 10))
    pou['Salud'] = minmax(pou['Salud'] + random.randint(0, 5))
    pou['Edad'] -= 1

def comer(pou):
    pou['Hambre'] = minmax(pou['Hambre'] - random.randint(5, 10))
    pou['Energia'] = minmax(pou['Energia'] + random.randint(10, 20))
    pou['Felicidad'] = minmax(pou['Felicidad'] + random.randint(5, 10))
    pou['Salud'] = minmax(pou['Salud'] + random.randint(0, 5))
    pou['Edad'] += 1

def morir(pou):
    pou['Estado'] = False

toto = iniciar("Churumbel")
estado(toto)

while toto['Estado']:
    option = input("¿Que quieres que haga? (jugar, comer, dormir, salir): ")
    estado(toto)

    if option == "jugar":
        jugar(toto)
    elif option == "comer":
        comer(toto)
    elif option == "dormir":
        dormir(toto)
    
    if toto['Salud'] <= 0:
        print("Tu Pou ha muerto.")
        morir(toto)
        break

    elif option == "salir":
        break
