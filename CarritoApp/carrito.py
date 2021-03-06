class Carrito:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')

        if not carrito:
            self.carrito = self.session['carrito'] = {}
        else:
            self.carrito = carrito

    def agregarProducto(self, producto):

        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "id_producto": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break

        self.guardar()

    def eliminarProducto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar()

    def restarCantidadProducto(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                if int(value["cantidad"]) > 1:
                    value["cantidad"] = value["cantidad"] - 1
                    value["precio"] = float(value["precio"]) - producto.precio
                    break
                else:
                    self.eliminarProducto(producto)    
                    break
        self.guardar()

    def vaciarCarrito(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True