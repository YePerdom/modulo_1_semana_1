# Se hace una bienvenida al usuario.
print("")
bienvenida = """Bienvenido a la tienda.
Esperamos que haya tenido una gradable estadía.
Por favor ingrese los datos necesarios para finalizar su compra."""
print(bienvenida)

# Se solicitan los datos del producto a comprar, tales como: Nombre del producto, Valor del producto y porcentaje de descuento (si aplica).
print("")
nombre_de_cliente = (input("Ingrese tu nombre completo: "))
n_identificacion = input("Ingrese su número de identificación: ")
producto = input("Ingrese el nombre del producto que desea llevar: ")
valor_unid = float(input("Ingrese el valor del producto (sin puntos o comas): "))
cantidad = float(input("Ingrese la cantidad de productos: "))
descuento = float(input("Indique la  cantidad de descuento correspondiente (si aplica y sin símbolos): "))

# Se hace un resumen de los datos indicados por el cliente,  y numero de identificación
print("")
print("RESUMEN DE COMPRA")

# Si le cliente no indica su nombre, indicar que es Cliente consumidor
if nombre_de_cliente == '':
    nombre_de_cliente = "Cilente consumidor."
    
# Si el ciente no indica numero de identificación indicar que su numero de identificación será "222222222"
if n_identificacion == '':
    n_identificacion = 222222222
    
#Utilizamos el precio, cantidad y decuento para  calcualar el valor total a pagar por el ciente    
valor_neto = valor_unid * cantidad
valor_descontado = (valor_neto * descuento) / 100 
valor_total = valor_neto - valor_descontado
    
print(f"Nombre del cliente: {nombre_de_cliente}")
print(f"Número de identificación: {n_identificacion}")
print(f"Producto: {producto}")
print(f"Valor unitario: {valor_unid:.2f}")
print(f"Cantidad de productos: {cantidad:.0f}")
print(f"Valor neto: {valor_neto:.2f}")
print(f"Porcentaje de descuento: {descuento:.2f}%")
print(f"Total descuento: {valor_descontado:.2f}")
print(f"Valor total: {valor_total:.2f}")

#Detalles de compra
print("")
print(f"------- DETALLES ------")
print(f"Detalle del producto_ _ _ _ _ Valor unit._ _ _ _ cant._ _ _ _ valor tot.")
print(f"{producto}_ _ _ _ {valor_unid}_ _ _ _ {cantidad}_ _ _ _ {valor_total}")