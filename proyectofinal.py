import random
import gi 
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
import matplotlib . pyplot as plt
import numpy as np
from matplotlib . patches import Patch  
import csv
import re
archivo="reporte.csv"
#clase bacteria
class Bacteria():
    #inicializacion de datos 
    def __init__(self):
        self.id=random.randint(10,2000)
        self.raza=None
        self.energia=random.randint(111,999)
        self.resistente=False
        self.estado=True
    #funciones para colocar los datos
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

    def random_raza(self):
        n=random.randint(1,3)
        R=None
        if n==1:
            R="cocos"
        elif n==2:
            R="Bacilo"
        elif n==3:
            R="Espirilos"
        else:
            print("Error al crear raza")
            return
        return R

    def random_resistencia(self):
        n=random.randint(1,2)
        if n==1:
            es=True
        elif n==2:
            es=False
        else:
            print("Erro al crear random en resistencia")
            return
        return es

    #crea una bacteria
    def crear_bacteria(self,raza,resistencia):
        self.set_raza(raza)
        self.set_resistente(resistencia)
    #comprobacion de si existen nutrientes para alimentar a las bacterias
    def Alimentar(self,Nutrientes_Ambiente,Nutrientes_a_consumir):
        if Nutrientes_Ambiente>=Nutrientes_a_consumir:
            self.energia+=Nutrientes_a_consumir
            print(f"La bacteria {self.id} Se ha alimentado {Nutrientes_a_consumir} nutrientes")  
        else:
            print(f"La bacteria {self.id} no consumio, ya que no se puede consumir mas nutrientes de los que hay en al celda")
    #crea una nueva bacteria a partir de una ya existente
    def dividirse(self):
        if self.energia>=500:
            Nueva_celula= Bacteria()
            self.energia=self.energia//2
            Nueva_celula.crear_bacteria(self.raza,self.resistente)
            Nueva_celula.set_energia(self.energia)
            return Nueva_celula
    #random para mutacion de resistencia a antibioticos
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
    #si pierde energia se muere
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
#clase ambiente
class Ambiente():
    def __init__(self):
        self.grilla=None
        self.nutrientes=random.randint(100,1000)
        self.factor_ambiental=None
        self.posicion=[]

    def set_nutrientes(self,N):
        if isinstance(N,int):
            self.nutrientes=N
    #actuializa la energia las bacterias con la del ambiente
    def actualizar_nutrientes(self,nutriente):
        for posicion in self.posicion:
            for bacteria in posicion.bacterias:
                bacteria.energia+=nutriente       
    #crea un random para agregar nutrientes
    def difundir_nutrientes(self):
        nuevos_nutrientes=random.randint(10,500)
        self.nutrientes+=nuevos_nutrientes
    #sin definir
    def aplicar_ambiente(self,n):
        pass
    #crea un valor random para agregar una posicion aleatoria
    def crear_espacio(self,n,k):
        while n>0:
            a=random.randint(0,4)
            b=random.randint(0,4)
            if [a,b]in self.posicion:
                return
            else:
                self.posicion.append([a,b,k])
                n=n-1
    
                    
#clase colonia
class Colonia():
    def __init__(self):
        self.Bacterias=[]
        self.Ambiente=None
        self.lugar=[1,1]
        self.tipo=1 #inicializa en 1 que significa que es bacteria
    
    def set_Ambiente(self,ambiente):
        self.Ambiente=ambiente

    def set_lugar(self,posicion):
        self.lugar=posicion    

    #agrega bacteria a la colonia
    def agregar_bacteria(self,Bacteriaa):
        self.Bacterias.append(Bacteriaa)

    def crear_colonia(self):
        nueva_colonia=Colonia()
        for Bacteria in self.Bacterias:
            if Bacteria.energia>=500:
                nueva_bacteria=Bacteria.dividirse()
                nueva_colonia.agregar_bacteria(nueva_bacteria)
        return nueva_colonia
    #comprobacion de movimiento de la colonia en el ambiente
    def paso(self):
        for i in range(len(self.Bacterias)):
            self.Bacterias[i].energia-=10
            self.Bacterias[i].morir()
        if len(self.Bacterias) > 0:
            mov = random.randint(1, 4)
            x=self.lugar[0]
            y=self.lugar[1]
            if mov == 1 and x < 4: 
                self.lugar[0] += 1
            elif mov == 2 and y < 4:  
                self.lugar[1] += 1
            elif mov == 3 and x > 0: 
                self.lugar[0] -= 1
            elif mov == 4 and y > 0:  
                self.lugar[1] -= 1
    #reporte de si existen bacterias vivas o estan muertas en la casilla             
    def reporte_estado(self):
        suma_estados=0
        for i in Bacterias:
            if Bacterias[i]==True:
                suma_estados+=1
            else:
                suma_estados+=0
            total_bacterias=+1
        print(f"La cantidad de bacterias que hay vivas son {suma_estados}, de un total de {total_bacterias}")
    
    #exportacion de archivo cvs
    def exportar_csv(self,archivo):
        with open(archivo,mode='w',newline='',encoding='utf-8')as archivo_csv:
            escritor=csv.writer(archivo_csv)
            escritor.writerow([
                'id_bacteria', 
                'raza', 
                'energia', 
                'es_resistente', 
                'esta_viva', 
            ])
            for bacteria in self.Bacterias:
                fila = [
                    bacteria.id,
                    bacteria.raza,
                    bacteria.energia,
                    bacteria.resistente,
                    bacteria.estado,
                ]
                escritor.writerow(fila)


QUIT = False

def quit_(window):
    global QUIT
    QUIT = True

class simulacion(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.ejemplo.App")
    
    def crear_grillas(self,ambiente):
        #crea grilla vacia
        grilla = np.zeros((5, 5))
        #añade a cada punto distinto un dato de una colonia 
        for i in range(len(ambiente.posicion)):
            print(ambiente.posicion[i])
            x=ambiente.posicion[i][0]
            y=ambiente.posicion[i][1]
            k=ambiente.posicion[i][2]
            if grilla[x,y]==0:
                grilla[x,y]=k
        print(grilla)
        return grilla

    def do_activate(self):
        self.window = Gtk.ApplicationWindow(application=self)
        self.window.set_title("Lab de Bacterias simuladas")
        self.window.set_default_size(480, 360)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window.set_child(box)

        self.Colonias_iniciales= Gtk.Entry()
        self.Colonias_iniciales.set_text("Indique la cantidad de Colonias que quiere comenzar")
        box.append(self.Colonias_iniciales)

        self.Bacterias_iniciales = Gtk.Entry()
        self.Bacterias_iniciales.set_text("Indique con cuantas bacterias por colonia quiere comenzar")
        box.append(self.Bacterias_iniciales)
        
        self.Antibioticos=Gtk.Entry()
        self.Antibioticos.set_text("Indique cuantos antibioticos quiere colocar")
        box.append(self.Antibioticos)

        self.Cantidad_de_pasos=Gtk.Entry()
        self.Cantidad_de_pasos.set_text("Indique cuantos pasos va a realizar")
        box.append(self.Cantidad_de_pasos)

        self.Boton_Iniciar = Gtk.Button(label="Registrar")
        self.Boton_Iniciar.connect("clicked", self.Iniciar_clicked)
        box.append(self.Boton_Iniciar)

        self.window.show()

    def Iniciar_clicked(self,Button):
        Colonias=self.Colonias_iniciales.get_text()
        Bacterias=self.Bacterias_iniciales.get_text()
        Antibioticos=self.Antibioticos.get_text()
        Pasos=self.Cantidad_de_pasos.get_text()
        if not re.fullmatch(r"[0-9]+", Colonias):
            self.mostrar_dialogo("Error","La cantidad de colonias debe ser un numero entero")
            return
        if not re.fullmatch(r"[0-9]+", Bacterias):
            self.mostrar_dialogo("Error","La cantidad de bacterias debe ser un numero entero")
            return
        if not re.fullmatch(r"[0-9]+", Antibioticos):
            self.mostrar_dialogo("Error","La cantidad de antibioticos debe ser un numero entero")
            return
        if not re.fullmatch(r"[0-9]+", Pasos):
            self.mostrar_dialogo("Error","La cantidad de bacterias debe ser un numero entero")
            return
        else:
            n=int(Bacterias)
            m=int()
            ambiente_simulado=Ambiente()
            while m>0:
                temp_colonia=colonia()
                while n>0:
                    temp_bacteria=Bacteria()
                    Raz=Bacteria.random_raza()
                    es=Bacteria.random_resistencia()
                    temp_bacteria=temp_bacteria.crear_bacteria(Raz,es)
                m-=1
                agregar_bacteria(temp_bacteria)                
            self.crear_grillas()

    def mostrar_dialogo(self, title, message):
        dialogo = Gtk.MessageDialog(
            transient_for=self.window,
            modal=True,
            title=title,
            text=message,
            buttons=Gtk.ButtonsType.OK,
        )
        dialogo.connect("response",self.cerrar_dialogo)
        dialogo.present()
    def cerrar_dialogo(self, widget, action):
        widget.destroy()



            
    


    


    

        
        

#main    
ambiente=Ambiente()
Bacteria1=Bacteria()
print(Bacteria1.energia)
Bacteria2=Bacteria()
Bacteria1.crear_bacteria("a",True)
Bacteria2.crear_bacteria("b",False)
Bacteria1.Alimentar(ambiente.nutrientes,400)
Bacteria2.Alimentar(ambiente.nutrientes,100)
Bacteria3=Bacteria()
print(Bacteria3.raza)
Bacteria3=Bacteria1.dividirse()
print(Bacteria1.energia)
print(Bacteria3.raza)
print(Bacteria3.energia)
Bacteria3.morir()
colonia=Colonia()
colonia.agregar_bacteria(Bacteria1)
colonia.agregar_bacteria(Bacteria2)
colonia.agregar_bacteria(Bacteria3)
ambiente.crear_espacio(10,1)
ambiente.crear_espacio(2,2)
colonia.lugar=ambiente.posicion[0]
print(colonia.lugar)
colonia.paso()
print(colonia.lugar)
a=simulacion.crear_grillas(None,ambiente)

if __name__ == "__main__":
    app = simulacion()
    app.run()


