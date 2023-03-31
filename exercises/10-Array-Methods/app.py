names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE


def sort_names(lista):
    lista.sort()
    return lista

print(sort_names(names))

# copy_list = names[:] # METODO PARA COPIAR LISTAS Y STRING, LIKE SPLICE, SE PUEDE PONER ARGUMENTOS ANTES Y DESPUES DE
# LOS ":" PARA INDICAR INDICE INICIAL Y FINAL (ESTE ULTIMO SIN INCLUIR)


# OTRA SOLUCION
# SORTED SI DEVUELVE UN ARRAY NUEVO Y NO MODIFICA EL ORIGINAL, NO COMO SORT(), TAMBIEN ADMITE PARAMETROS Y KEY
# def sort_names(lista):
#     return sorted(lista)

# print(sort_names(names))