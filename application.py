#-*- coding: utf-8 -*-
"Este programa simula una máquina registradora"
print "                            Bienvenido a Tienda"
print        """
                 88      a8P          db         88b           d88  
                 88    ,88'          d88b        888b         d888  
                 88  ,88"           d8'`8b       88`8b       d8'88  
                 88,d88'           d8'  `8b      88 `8b     d8' 88  
                 8888"88,         d8YaaaaY8b     88  `8b   d8'  88  
                 88P   Y8b       d8        8b    88   `8b d8'   88  
                 88     "88,    d8'        `8b   88    `888'    88  
                 88       Y8b  d8'          `8b  88     `8'     88  
                                                                   """
print "                         Seleccione la opción que desea.\n"
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
            if precio > 0 and cantidad > 0:
                break
            else:
                pass
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
            b = int(raw_input("Ingrése la cantidad:\n"))
            if b > 0:
                cliente[a] = b #ingresará el producto y la cantidad
                calc = float(inventario[a]) - float(cliente[a])
                inventario[a] = calc
                total = float(precios[a]) * float(cliente[a]) #precio por la cantidad que ingresó
                lista.append(total) #ingrésa un valor a lista
                break
            else:
                pass
        except KeyError:
            print "Este producto no esta en existencia en inventario, intente nuevamente\n"
            break

#Factura
def factura():
    raw_input("Ingrése Nombre y Apellido:")
    raw_input("ingrése No. nit:")
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
        opcion = raw_input("> ")
    total = sum(lista)
    iva = 0.12
    gold = 0.05
    silver = 0.02
    calc_iva = float(total) * iva #Calcula el iva
    iva_agregado = float(calc_iva) + float(total) #Agrega el iva
    if opcion == 1: #no hace descuento
        print "El total de su cuenta es \n%.2f\nmas el IVA \n%.2f\n" % (total, calc_iva)
        print "El total a pagar es %.2f \n" % iva_agregado
        respuesta = 0
        raw_input("Presione enter para continuar... ")
    elif opcion == 2: #Descuento Gold
        calc_gold = float(iva_agregado) * float(gold)
        desc_gold = float(iva_agregado) - float(calc_gold)
        print """El total de su cuenta es \n%.2f\nmás IVA \n%.2f\ny su descuento en¸
tarjeta GOLD de \n%.2f\n""" % (round(total, 2), round(calc_iva, 2), round(desc_gold, 2))
        print "El total a pagar es %.2f \n" % round(desc_gold, 2)
        respuesta = 0
        raw_input("Presione enter para continuar...")
    elif opcion == 3: #Descuento
        calc_silver = float(iva_agregado) * float(silver)
        desc_silver = float(iva_agregado) - float(calc_silver)
        print """El total de su cuenta es \n%.2f\nmás IVA \n%.2f\ny su descuento en¸
tarjeta SILVER de \n%.2f\n""" % (round(total, 2), round(calc_iva, 2), round(calc_silver, 2))
        print "El total a pagar es %.2f \n" % round(desc_silver, 2)
        respuesta = 0
        raw_input("Presione enter para continuar...")

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
        print "                          '''''Gracias por su preferencia'''''\n"
        respuesta = 1
    else:
        print "ingrese una opción 1 al 4, no se ingrése letras \n"
