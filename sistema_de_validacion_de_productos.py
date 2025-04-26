# Se hace una bienvenida al usuario.
print("")
bienvenida = """Bienvenid@ a la tienda.
Esperamos que haya tenido una gradable estadía.
Por favor ingrese los datos necesarios para finalizar su compra."""
print(bienvenida)

# Se solicitan los datos del producto a comprar, tales como: Nombre del producto, Valor del producto y porcentaje de descuento (si aplica).
print("")
nombre_de_cliente = (input("Ingrese su nombre completo: "))
n_identificacion = input("Ingrese su número de identificación: ")

producto = input("Ingrese el nombre del producto que desea llevar: ")

# Se valida que se haya ingresado un producto de lo contrario se le volverá a pedir al ususario.
while producto == '' or producto == ' ':
    print("No ha indicado el nombre del producto")
    producto = input("Por favor ingrese el nombre del producto: ")

# Se valida que el dato ingresado sea un numero y que no se deje la variable vacia.
while True:
    valor_unid = (input("Ingrese el valor del producto (sin puntos ni comas): "))
    try:
        valor_unid = float(valor_unid)
        break  
    except ValueError:
        print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Se valida que no sea posible ingresar numeros menores que 0.
while valor_unid < 0:
    print("Error, ha indicado un valor incorrecto")
    while True:
        valor_unid = (input("Indique correctamente el valor del producto (sin puntos ni comas): "))
        try:
            valor_unid = float(valor_unid)
            break  
        except ValueError:
            print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Se valida que el dato ingresado sea un numero y que no se deje la variable vacia.
while True:
    cantidad = (input("Ingrese la cantidad de productos: "))
    try:
        cantidad = float(cantidad)
        break  
    except ValueError:
        print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Se valida que no sea posible ingresar numeros menores que 0.
while cantidad < 0:
    print("Error, ha indicado un número incorrecto")
    while True:
        cantidad = (input("Indique cantidad de productos: "))
        try:
            cantidad = float(cantidad)
            break  
        except ValueError:
            print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Se valida que el dato ingresado sea un numero y que no se deje la variable vacia.
while True:
    descuento = (input("Indique la  cantidad de descuento correspondiente (si aplica y sin símbolos): "))
    try:
        descuento = float(descuento)
        break  
    except ValueError:
        print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Se valida que no sea posible ingresar numeros menores que 0 o mayores que 100.
while descuento < 0 or descuento > 100:
    print("Error, ha indicado un valor incorrecto")
    while True:
        descuento = (input("Indique correctamente el descuento del producto (sin puntos ni comas): "))
        try:
            descuento = float(descuento)
            break  
        except ValueError:
            print("Ha ingresado un carácter inválido. Intente de nuevo.")

# Si le cliente NO indica su nombre, indicar que es Cliente consumidor
if nombre_de_cliente == ''or nombre_de_cliente == ' ':
    nombre_de_cliente = "Cilente consumidor."
    
# Si el ciente NO indica numero de identificación indicar que su numero de identificación será "222222222"
if n_identificacion == '' or n_identificacion == ' ':
    n_identificacion = 222222222
    
#Utilizamos el precio, cantidad y decuento para  calcualar el valor total a pagar y el descuento total para el ciente    
valor_neto = valor_unid * cantidad
valor_descontado = (valor_neto * descuento) / 100 
valor_total = valor_neto - valor_descontado

# Se hace un resumen de los datos indicados por el cliente y se detalla la compra.
print("")
print("RESUMEN DE COMPRA")
print(f"Nombre del cliente: {nombre_de_cliente}")
print(f"Número de identificación: {n_identificacion}")
print(f"Producto: {producto}")
print(f"Valor unitario: {valor_unid:.2f}")
print(f"Cantidad de productos: {cantidad:.0f}")
print(f"Valor neto: {valor_neto:.2f}")
print(f"Porcentaje de descuento: {descuento:.2f}%")
print(f"Total descuento: {valor_descontado:.2f}")
print(f"Valor total: {valor_total:.2f}")