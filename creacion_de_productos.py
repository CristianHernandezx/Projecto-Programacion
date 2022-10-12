class Producto: #La clase Producto permite crear un producto con toda su informacion y añadirlo a un inventario
    def __init__ (self, Inventario, Nombre, Codigo, Unidades, PrecioCompra, PrecioVenta, UnidadesVitrina, UnidadesBodega): #"Inventario" es una lista donde se guardaran objetos de la clase Producto
        self.nombre = Nombre
        self.cod = Codigo
        self.und = Unidades
        self.precio_compra = PrecioCompra
        self.precio_venta = PrecioVenta
        self.gasto = PrecioCompra*Unidades
        self.ingreso_proyectado = PrecioVenta*Unidades
        
        if UnidadesBodega + UnidadesVitrina == Unidades:
            self.und_vitrina = UnidadesVitrina
            self.und_bodega = UnidadesBodega
        else:
            print("La cantidad de unidades en vitrina y bodega deben coincidir con la cantidad total del producto.")
        Inventario.append(self)
        
    def agregar_unidades(self, n): #n es la cantidad de unidades que se agregará del producto. Por defecto se almacenan en la bodega.
        self.und += n
        self.und_bodega += n
        
        self.gasto = self.gasto + (n*self.precio_compra)
        self.ingreso_proyectado = self.ingreso_proyectado + (n*self.precio_venta)
        
    def cambiar_precio(self, nuevo_precio):
        self.precio_venta = nuevo_precio
        
    def sacar_a_vitrina(self,n):  #n es las unidades de producto que se llevarán de la bodega a la vitrina
        if n<self.und_bodega:
            self.und_vitrina += n
            self.und_bodega -= n
        else: 
            print("En bodega no hay unidades suficientes para llevar a la vitrina.")
            
    def __str__ (self):
        msn = "Producto: {0} \nCódigo: {1} \nUnidades: {2} \n\tVitrina: {3}\n\tBodega: {4} \nPrecio de Compra: {5} \nPrecio de Venta: {6}".format(self.nombre, self.cod, self.und, self.und_vitrina, self.und_bodega, self.precio_compra, self.precio_venta)
        return msn
        
    def guardar_en_bodega (self, n): #n es las unidades de producto que se llevrán de la vitrina a la bodega
        if n<self.und_vitrina:
            self.und_vitrina -= n
            self.und_bodega += n
        else: 
            print("En vitrina no hay unidades suficientes para llevar a la bodega.")      
            
class Caja:
     def __init__ (self, numero_de_caja, efectivo_inicial):
        self.num_caja= numero_de_caja
        self.efectivo_inicial = efectivo_inicial
        self.efectivo_total = efectivo_inicial
        
    def venta(self,  producto):
        producto.und -= 1
        if producto.und_vitrina > 0:
            producto.und_vitrina -= 1
        elif producto.und_vitrina == 0 and producto.und_bodega > 0:
            print("Producto en bodega")
        else:
            print("Producto agotado")
