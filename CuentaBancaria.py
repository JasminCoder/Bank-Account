class CuentaBancaria:

    todas_las_instancias = []

# ¡No olvides agregar algunos valores predeterminados para estos parámetros!

    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.todas_las_instancias.append(self)


    
    def deposito(self, monto):
        self.balance += monto
        return(self)
        


    def retiro(self, amount):
        self.balance -= amount
        return(self)    



    def mostar_info_cuenta(self):
        print(f"Su nuevo balance es $ {self.balance}")
        return(self)



    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interés/12
        return(self)


    @classmethod #para la clase completa
    def cuenta(cls):

        for i in cls.todas_las_instancias:
            print(f"Su balance total es $ {i.balance}")
