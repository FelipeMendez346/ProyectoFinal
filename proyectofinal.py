import random

class Bacteria():
    def __init__(self):
        self.id=random.randint(10,2000)
        self.raza=None
        self.energia=random.randint(111,999)
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
        if isinstance(es,bool):
            self.resistente=es
    def set_estado(self,vivo):
        if isinstance(vivo,bool):
            self.estado=vivo

    def crear_bacteria(self,raza,energia,resistencia):
        self.set_raza(raza)
        self.set_energia(energia)
        self.set_resistente(resistencia)

    def Alimentar(self,Nutrientes_Ambiente,Nutrientes_a_consumir):
        if Nutrientes_Ambiente>=Nutrientes_a_consumir:
            self.energia+=Nutrientes_a_consumir
            print(f"La bacteria {self.id} Se ha alimentado {Nutrientes_a_consumir} nutrientes")  
        else:
            print(f"La bacteria {self.id} no consumio, ya que no se puede consumir mas nutrientes de los que hay en al celda")

    def dividirse(self):
        if self.energia>=500:
            Nueva_celula= Bacteria()
            Nueva_celula.crear_bacteria(self.raza,self.energia/2,self.resistente)
            self.energia=self.energia/2
            return Nueva_celula
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
        if self.energia<=100 and self.estado==True:
            self.estado=False
            print("La Bacteria a muerto")
            return           
        if self.estado==True:
            print("La Bacteria sigue viva")
            return
        else:
            print("la Bacteria esta muerta")

class Ambiente():
    def __init__(self):
        self.grilla=None
        self.nutrientes=0
        self.factor_ambiental=None

    def actualizar_nutrientes(self):
        pass

    def difundir_nutrientes(self):
        pass
    def aplicar_ambiente(self):
        pass

class Colonia():
    def __init__(self):
        self.Bacterias=[]
        self.Ambiente=None

    def paso():
        pass

    def reporte_estado():
        pass

    def exportar_csv():
        pass
    

#main    
    
Bacteria1=Bacteria()
Bacteria2=Bacteria()
Bacteria1.crear_bacteria("a",Bacteria1.energia,True)
Bacteria2.crear_bacteria("b",Bacteria2.energia,False)
Bacteria1.Alimentar(200,100)
Bacteria2.Alimentar(50,100)
Bacteria3=Bacteria()
print(Bacteria3.energia)
Bacteria3.morir()
