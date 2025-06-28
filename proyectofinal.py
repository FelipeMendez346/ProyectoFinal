import random
import gi 
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
import matplotlib . pyplot as plt
import numpy as np
from matplotlib . patches import Patch  

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

    def crear_bacteria(self,raza,energiaa,resistencia):
        self.set_raza(raza)
        self.set_energia(energiaa)
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
            self.energia=self.energia//2
            Nueva_celula.crear_bacteria(self.raza,self.energia,self.resistente)
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
        self.nutrientes=random.randint(100,1000)
        self.factor_ambiental=None
        self.posicion=[]

    def set_nutrientes(self,N):
        if isinstance(N,int):
            self.nutrientes=N
    def actualizar_nutrientes(self):
        pass

    def difundir_nutrientes(self):
        nuevos_nutrientes=random.randint(10,500)
        self.nutrientes+=nuevos_nutrientes
    def aplicar_ambiente(self,n):
        pass
    def crear_espacio(self,n):
        while n>0:
            a=random.randint(0,5)
            b=random.randint(0,5)
            if [a,b]in posicion:
                return
            else:
                self.posicion.append([a,b])
                    

class Colonia():
    def __init__(self):
        self.Bacterias=[]
        self.Ambiente=None

    def paso():
        for i in Bacterias:
            Bacterias[i].energia-=10
            if Bacterias[i].energia<=100:
                Bacterias[i].morir

    def set_Ambiente(self,ambiente):
        self.Ambiente=ambiente
            

    def reporte_estado():
        suma_estados=0
        for i in Bacterias:
            if Bacterias[i]==True:
                suma_estados+=1
            else:
                suma_estados+=0
            total_bacterias=+1
        print(f"La cantidad de bacterias que hay vivas son {suma_estados}, de un total de {total_bacterias}")
        
    def exportar_csv():
        pass


QUIT = False

def quit_(window):
    global QUIT
    QUIT = True


class simulacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Simulacion")
        self.connect("close-request",quit_)

    grilla = np.zeros((5, 5))

    def crear_grillas(self,posiciones):
        

    
    cmap = plt.cm.get_cmap('Set1', 5)
    fig, ax = plt.subplots(figsize=(6, 6))
    cax = ax.matshow(grilla, cmap=cmap)

    legend_elements = [
        Patch(facecolor=cmap(1/5), label='Bacteria activa'),
        Patch(facecolor=cmap(2/5), label='Bacteria muerta'),
        Patch(facecolor=cmap(3/5), label='Bacteria resistente'),
        Patch(facecolor=cmap(4/5), label='Biofilm'),]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.45, 1))

    ax.set_xticks(np.arange(0, 5, 1))
    ax.set_yticks(np.arange(0, 5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    for i in range(5):
        for j in range(5):
            val = grilla[i, j]
            if val > 0:
                ax.text(j, i, int(val), va='center', ha='center', color='white')
    plt.title("grilla 5x5")
    plt.tight_layout()
    plt.show()


    


    

        
        

#main    
ambiente=Ambiente()
Bacteria1=Bacteria()
print(Bacteria1.energia)
Bacteria2=Bacteria()
Bacteria1.crear_bacteria("a",Bacteria1.energia,True)
Bacteria2.crear_bacteria("b",Bacteria2.energia,False)
Bacteria1.Alimentar(ambiente.nutrientes,400)
Bacteria2.Alimentar(ambiente.nutrientes,100)
Bacteria3=Bacteria()
print(Bacteria3.raza)
Bacteria3=Bacteria1.dividirse()
print(Bacteria1.energia)
print(Bacteria3.raza)
print(Bacteria3.energia)
Bacteria3.morir()
