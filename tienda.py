from producto import Producto

class Tienda:
  def __init__(self, nombre, costo_delivery):
    self.__nombre = nombre
    self.__listado_productos = []
    self.__costo_delivery = costo_delivery
  
  @property
  def nombre(self):
    return self.__nombre
  
  @property
  def listado_productos(self):
    return self.__listado_productos
  
  @property
  def costo_delivery(self):
    return self.__costo_delivery


  def producto_ingresado(self, producto):
    for i in self.__listado_productos:
      if i.nombre == producto.nombre:
        i.modificar_stock(producto.stock)
        break
      else:
        self.__listado_productos.append(producto)
  
  def lista_productos(self):
    lista=""
    for producto in self.listado_productos:
      lista += f"{producto.nombre} - Precio: ${producto.precio}"
      if isinstance(self, Supermercado) and producto.stock < 10:
        lista += " (Pocos productos disponibles)"
        if isinstance(self, Farmacia) and producto.precio > 15000:
          lista += "(Envío gratis al solicitar este producto)"
          lista += "\n"
    return lista.strip()
  
  def realizar_venta(self, nombre_producto, cantidad):
    for producto in self.listado_productos:
      if producto.nombre == nombre_producto:
        if isinstance(self, Farmacia) and cantidad > 3:
          print("No se puede vender más de 3 unidades en una farmacia.")
          return
        if cantidad <= producto.stock:
          producto.modificar_stock(-cantidad)
        else:
          print("No hay suficiente stock disponible para realizar la venta.")
        return
    print("El producto no está disponible en la tienda.")

class Restaurante(Tienda):
  pass

class Supermercado(Tienda):
  pass

class Farmacia(Tienda):
  pass

