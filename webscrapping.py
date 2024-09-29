import timeit

import bs4
import requests
import time

# Crear URL sin numero de pagina usando .format
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []


def webscrapping_ejemplo():

    # iterar paginas
    for pagina in range(1, 51):

        # crear sopa en cada pagina
        url_pagina = url_base.format(pagina)
        resultado = requests.get(url_pagina)
        sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

        # seleccionar datos de los libros
        libros = sopa.select('.product_pod')

        # iteracion por cada libro
        for libro in libros:

            # Crear la condicion para que nos muestre libros con 4 o 5 estrellas y su titulo
            if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

                # guardar titulo en una variable
                titulo_libro = libro.select('a')[1]['title']
                print(titulo_libro)

                # agregar a la lista
                titulos_rating_alto.append(titulo_libro)

    # ver libros de 4 o 5 estrellas en consola
    for t in titulos_rating_alto:
        print(t)


inicio = timeit.timeit()

webscrapping_ejemplo()

final = timeit.timeit()

duracion = inicio-final

print('\n')
print('*' * 30 + ' Duracion de la ejecucion del codigo ' + '*' * 30)
print('\n')

print(duracion)




