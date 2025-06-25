import random

class Bacteria():
    def __init__(self):
        self.id=random.randint(111,999)
        self.raza=None
        self.energia=0
        self.resistente=False
        self.estado=True
    
    def set_id(self,id):
        if isinstance(id,int):
            self.id=id
    def set_raza(self,raza):
        if isinstance(raza,str):
            self.raza=raza
    def set_energia(self,energia):
        if isinstance(energia,int):
            self.energia=energia
    def set_resistente(self,es):
        if isinstance(resistente,bool):
            self.resistente=es
    def set_estado(self,vivo):
        if isinstance(estado,bool):
            self.estado=vivo

    def crear_bacteria(self,id,raza,energia,resistencia,estado):
        self.set_raza(raza)
        self.set_energia(energia)
        self.set_resistente(resistencia)
        self.set_estado(estado)

    def Alimentar(self,Nutrientes_Ambiente,Nutrientes_a_consumir):
        if Nutrientes_Ambiente>=Nutrientes_a_consumir:
            self.energia+=Nutrientes_a_consumir
        else:
            print("No se puede consumir mas nutrientes de los que hay en al celda")

    def dividirse(self):
        if self.energia>=500:
            Nueva_celula= Bacteria()
            Nueva_celula.crear_bacteria(self.raza,self.energia/2,self.resistente,True)
    def mutar(self):
        a=random.randint(1,10)
        if a==3 and self.resistente==True:
            self.resistente=False
            print("Se ha mutado y se ha quitado la resistencia a antibioticos")
        if a==7 and self.resistente==False:
            self.resistente=True
            print("Se ha mutado y se ha agregado la resistencia a antibioticos")
        else:
            print("No Muto la bacteria")
    
    def morir(self):
        if self.energia<=100:
            self.estado=False
            print("La Bacteria a muerto")
        if self.estado==True:
            print("La Bacteria sigue viva")
        else:
            print("la Bacteria esta muerta")

class Ambiente():
    def __init__(self):
        self.grilla=None
        self.nutrientes=0
        self.factor_ambiental=None

    def actualizar_nutrientes(self):

    def difundir_nutrientes(self):

    def aplicar_ambiente(self):


class Colonia():
    def __init__(self):
        self.Bacterias=[]
        self.Ambiente=None

    def paso():

    def reporte_estado():

    def exportar_csv():
    

#main    
    

