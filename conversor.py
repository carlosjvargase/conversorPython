#Conversor de Pesos a Dolares
#Admite pesos argentinos y pesos mexicanos.

#las funciones se recomiendan colocar arriba de tu codigo, para que cuando se ejecute este definida.

def conversor(tipo_Pesos, valor_Dolar):
    pesos = input('Cuantos pesos' + tipo_Pesos + 'tienes?: ')
    pesos = float(pesos)
    # float cambiar numero a decimal.
    dolares = pesos / valor_Dolar
    dolares = round(dolares, 2)
    # linea anterior, tomamos contenido y reducimos a 2 decimal, y guardamos en variables a dolares.
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

menu = '''
Bienvenido al conversor de monedas 💸

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: '''
#aqui guardaremos menu¨¨¨ Crea cadena de caracteres de varias lineas ¨¨¨¨

opcion = int(input(menu))
if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor('mexicanos', 24)
else:
    print('Ingresa una opción correcta por favor')




