class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
       
        self.carro=carro

    def agregar(self,mesa):
        if(str(mesa.id) not in self.carro.keys()):
            self.carro[mesa.id]={
                "producto_id":mesa.id,
                "nombre":mesa.nombre,
                "precio":str(mesa.precio),
                "cantidad":1,
                "imagen":mesa.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(mesa.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+mesa.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,mesa):
        mesa.id=str(mesa.id)
        if mesa.id in self.carro:
            del self.carro[mesa.id]
            self.guardar_carro()

    def restar_producto(self, mesa):
        for key, value in self.carro.items():
                if key==str(mesa.id):
                    value["precio"]=float(value["precio"])-mesa.precio
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(mesa)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True