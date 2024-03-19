from producto import Producto
from tienda import Tienda, Restaurante, Supermercado, Farmacia

def crear_producto():
  nombre = input("Ingrese el nombre del producto: ")
  precio = float(input("Ingrese el precio del producto: "))
  stock = int(input("Ingrese el stock del producto (opcional, dejar en blanco si es 0): ") or 0)
  return Producto(nombre, precio, stock)

def main():
  nombre_tienda = input("Ingrese el nombre de la tienda: ")
  costo_delivery = float(input("Ingrese el costo de delivery: "))
  tienda = Tienda(nombre_tienda, costo_delivery)

  while True:
    print("\nOpciones:")
    print("1. Ingresar producto")
    print("2. Lista de productos")
    print("3. Realizar venta")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción: ")
    print("Opción ingresada:", opcion)

    if opcion == "1":
      producto = crear_producto()
      tienda.producto_ingresado(producto)
      print("¡Producto ingresado con éxito!")
    elif opcion == "2":
      print("Listado de productos:")
      print(tienda.lista_productos())
    elif opcion == "3":
      nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
      cantidad = int(input("Ingrese la cantidad que desea vender: "))
      tienda.realizar_venta(nombre_producto, cantidad)
    elif opcion == "4":
      print("¡Gracias por usar nuestro programa!")
      break
    else:
      print("Opción inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()