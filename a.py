#coding: utf-8
"Este programa simula una máquina registradora"
print "                             Bienvenido a Tienda KAM\n"
print "                 Seleccione la opción que desea.\n"
precios = {}
inventario = {}
lista = []
#inventario
def limpiar():
    del lista[:]
    return lista
def funcion_uno():
    while True:
        producto = raw_input("Ingrése el nuevo producto:\n")
        if producto.isalpha():
            producto.lower()
            break
        else:
            print "Solo puedes ingrésar letras\n"
    while True:
        try:
            precio = float(raw_input("Ingrése precio:\n"))
            cantidad = int(raw_input("Ingrése cantidad existente:\n"))
            break
        except ValueError:
            print "Solo puede ingrésar números\n"
#ingrésa al diccionario el producto y precio
    precios[producto] = precio
    inventario[producto] = cantidad #agrega la cantidad y cantidad
for i in precios:
    print "\nUsted ingresó\n", i, "al inventario\n"
    print "Con un precio de\n", precios[i]
    print "Y una cantidad de\n", inventario[i]

#Caja
def calcular_factura():
    cliente = {}
    while True:
        try:
            a = raw_input("Ingrése producto:\n")
            b = raw_input("Ingrése la cantidad:\n")
            cliente[a] = b #ingresará el producto y la cantidad
            calc = inventario[a] - cliente[a]
            inventario[a] = calc
            total = precios[a] * cliente[a] #precio por la cantidad que ingresó
            lista.append(total) #ingrésa un valor a lista
            break
        except KeyError:
            print "Este producto no esta en existencia en inventario, intente nuevamente\n"

#Factura
def factura():
    print raw_input("Ingrése Nombre y Apellido:")
    print raw_input("ingrése No. nit:")
    print """
Elija una opción\n: 
1 No cuenta con tarjeta de cliente frecuente\n
2 Cuenta con tarjeta Gold\n
3 Cuenta con tarjeta silver\n
"""
#Menu
    while True:
        try:
            opcion = input("> ") #ingrésa la opción que desea
            break
        except (ValueError, NameError):
            print "Sólo puede ingrésar números, intenta nuevamente\n"
    while opcion >= 4:
        print "No entendí, debe ingresár un número del 1 al 3\n"
        opcion = input("> ")
    total = sum(lista)
    iva = 0.12
    gold = 0.05
    silver = 0.02
    calc_iva = total * iva #Calcula el iva
    iva_agregado = calc_iva + total #Agrega el iva
    if opcion == 1: #no hace descuento
        print "El total de su cuenta es %s mas el iva %s \n" % (total, calc_iva)
        print "El total a pagar es %s \n" % iva_agregado
        respuesta = 0
        while respuesta == 0:
            a = raw_input("Desea salir de facturación? Si o No:\n")
            b = a.lower()
            if b == "si":
                limpiar()
                respuesta = 1
            elif b == "no":
                break
                respuesta = 1
            else:
                print "Debe ingrésar una opción válida\n"
    elif opcion == 2: #Descuento Gold
        calc_gold = iva_agregado * gold
        desc_gold = iva_agregado - calc_gold
        print """El total de su cuenta es %s más iva %s con un descuento de
        tarjeta Gold de %s \n""" % (total, calc_iva, calc_gold)
        print "El total a pagar es %s \n" % desc_gold
        respuesta = 0
        raw_input("Para cotiunar presione enter... ")
"""
        while respuesta == 0:
            a = raw_input("Desea salir de facturación? Si o No:\n")
            b = a.lower()
            if b == "si":
                limpiar()
                respuesta = 1
            elif b == "no":
                break
                respuesta = 1
            else:
                print "Debe ingrésar una opción válida \n"
"""
    elif opcion == 3: #Descuento
        calc_silver = iva_agregado * silver
        desc_silver = iva_agregado - calc_silver
        print """El total de su cuenta es %s más iva %s y su descuento de
        tarjeta silver de %s \n""" % (total, calc_iva, calc_silver)
        print "El total a pagar es %s \n" % desc_silver
        respuesta = 0
        while respuesta == 0:
            a = raw_input("Desea salir de facturación? Si o No:\n")
            b = a.lower()
            if b == "si":
                limpiar()
                respuesta = 1
            elif b == "no":
                break
                respuesta = 1
            else:
                print "Debe ingrésar una opción válida! \n"

#Menú principal
respuesta = 0
while respuesta == 0:
    opcion = raw_input("""
        1 Inventario\n
        2 Caja\n
        3 Facturar\n
        4 Salir\n """)
    if opcion == "1": #funcion_uno

        funcion_uno()
        respuesta = 0
    elif opcion == "2": #calcularFactura()
        calcular_factura()
        respuesta = 0
    elif opcion == "3": #Factura()
        factura()
        respuesta = 0
    elif opcion == "4":
        print "Gracias por su preferencia\n"
        respuesta = 1
    else:
        print "ingrese una opción 1 al 4, no se ingrése letras \n"