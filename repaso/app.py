



class Operaciones_2:
    def __init__(self,a,b):
        self.primer_numero=a
        self.segundo_numero=b
    
    def restar(self):
        return self.primer_numero - self.segundo_numero

    def suma(self):
        return self.primer_numero + self.segundo_numero
    
resultado_3 = Operaciones_2(3,4)
print(resultado_3.suma())
