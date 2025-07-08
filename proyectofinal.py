import random
import gi 
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch  
import csv
import re
import matplotlib
matplotlib.use('GTK4Agg') 
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas 
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
        if self.energia>=500 and self.estado==True:
            Nueva_celula= Bacteria()
            self.energia=self.energia//2
            Nueva_celula.crear_bacteria(self.raza,self.resistente)
            Nueva_celula.set_energia(self.energia)
            return Nueva_celula
        else:
            pass
    #random para mutacion de resistencia a antibioticos
    def mutar(self):
        a=random.randint(1,10)
        if a<=4 and self.resistente==False:
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
    def morir_antibiotico(self):
        if self.resistente==True:
            return
        else:
            self.estado=False

#clase ambiente
class Ambiente():
    def __init__(self):
        self.grilla=None
        self.nutrientes=random.randint(100,1000)
        self.factor_ambiental=None
        self.posicion=[]
        self.colonias=[]

    def set_nutrientes(self,N):
        if isinstance(N,int):
            self.nutrientes=N

    def agregar_colonia(self,Col):
        if isinstance(Col,Colonia):
            self.colonias.append(Col)
    #actuializa la energia las bacterias con la del ambiente
    def actualizar_nutrientes(self,nutriente):
        for Colonia in self.colonias:
            for bacteria in Colonia.Bacterias:
                if bacteria.estado==True:
                    bacteria.energia+=nutriente/(len(self.colonias)*reporte_estado())       
    #crea un random para agregar nutrientes
    def difundir_nutrientes(self):
        nuevos_nutrientes=random.randint(10,500)
        self.nutrientes+=nuevos_nutrientes
    #si esta cerca de un antibiotico muta o muere
    def aplicar_ambiente(self):
        pass
    #crea un valor random para agregar una posicion aleatoria
    def crear_espacio(self, k):
            a = random.randint(0, 4)
            b = random.randint(0, 4)
            self.posicion.append([a, b, k])
            return [a, b, k]
    
                    
#clase colonia
class Colonia():
    def __init__(self):
        self.bacterias=[]
        self.ambiente=None
        self.lugar=[1,1]
        self.tipo=1 #inicializa en 1 que significa que es bacteria
    
    def set_Ambiente(self,ambiente):
        self.ambiente=ambiente

    def set_lugar(self,posicion):
        self.lugar=posicion

    def set_tipo(self,tipo):
        self.tipo=tipo 

    #agrega bacteria a la colonia
    def agregar_bacteria(self,Bacteriaa):
        self.bacterias.append(Bacteriaa)

    def crear_colonia(self):
        nueva_colonia=Colonia()
        for Bacteria in self.bacterias:
            if Bacteria.energia>=500:
                nueva_bacteria=Bacteria.dividirse()
                nueva_colonia.agregar_bacteria(nueva_bacteria)
        nueva_colonia.set_Ambiente(self.ambiente)
        nueva_colonia.set_tipo=self.tipo
        return nueva_colonia
    #comprobacion de movimiento de la colonia en el ambiente
    def paso(self):
        self.reporte_estado()
        for i in range(len(self.bacterias)):
            self.bacterias[i].energia-=10
            self.bacterias[i].morir()
            self.bacterias[i].mutar()
        if self.reporte_estado()==0:
            self.lugar[2]==2
        if len(self.bacterias) > 0:
            mov = random.randint(1, 4)
            x=self.lugar[0]
            y=self.lugar[1]
            if mov == 1 and x < 4:
                NC=self.crear_colonia()
                NC.set_lugar(self.lugar[0]+1)
            elif mov == 2 and y < 4:
                NC=self.crear_colonia()
                NC.set_lugar(self.lugar[1]+1)  
            elif mov == 3 and x > 0:
                NC=self.crear_colonia()
                NC.set_lugar(self.lugar[0]-1) 
            elif mov == 4 and y > 0:
                NC=self.crear_colonia()
                NC.set_lugar(self.lugar[1]-1)
            else:
                for Bacteria in self.bacterias:
                    self.bacterias.append(Bacteria.dividirse(Bacteria))
            self.ambiente.difundir_nutrientes()

    #reporte de si existen bacterias vivas o estan muertas en la casilla             
    def reporte_estado(self):
        suma_estados=0
        total_bacterias = 0
        resiste=0
        for bacteria in self.bacterias:
            if bacteria.estado==True:
                suma_estados += 1
            if bacteria.es_resistente==True:
                resiste+=1
            total_bacterias+=1
        if resiste==suma_estados:
            self.tipo=3            
        print(f"La cantidad de bacterias que hay vivas son {suma_estados}, de un total de {total_bacterias}")
        return total_bacterias
    
    #exportacion de archivo cvs
    
            


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
        self.window.set_default_size(720, 480)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window.set_child(box)

        self.Colonias_iniciales= Gtk.Entry()
        self.Colonias_iniciales.set_text("3")
        box.append(self.Colonias_iniciales)

        self.Bacterias_iniciales = Gtk.Entry()
        self.Bacterias_iniciales.set_text("3")
        box.append(self.Bacterias_iniciales)
        
        self.Antibioticos=Gtk.Entry()
        self.Antibioticos.set_text("3")
        box.append(self.Antibioticos)

        self.Cantidad_de_pasos=Gtk.Entry()
        self.Cantidad_de_pasos.set_text("3")
        box.append(self.Cantidad_de_pasos)

        self.Boton_Iniciar = Gtk.Button(label="Iniciar")
        self.Boton_Iniciar.connect("clicked", self.Iniciar_clicked)
        box.append(self.Boton_Iniciar)

        self.window.show()

    def exportar_csv(self, archivo, ambiente, pasos):
        with open(archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(['id_bacteria', 'raza', 'energia', 'es_resistente', 'esta_viva'])
            for paso in range(pasos):
                for colonia in ambiente.colonias:
                    escritor.writerow([f"Colonia en [{colonia.lugar[0]},{colonia.lugar[1]}]"])
                    for Bacteria in colonia.bacterias:
                        escritor.writerow([
                            Bacteria.id,
                            Bacteria.raza,
                            Bacteria.energia,
                            Bacteria.resistente,
                            Bacteria.estado
                        ])
                    colonia.paso()
                self.recolectar_datos(paso+1, ambiente)
    
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
            m=int(Colonias)
            o=int(Antibioticos)
            p=int(Pasos)
            ambiente_simulado=Ambiente()
            while m > 0:
                temp_colonia = Colonia()
                temp_colonia.lugar = ambiente_simulado.crear_espacio(1)
                for _ in range(n):
                    temp_bacteria = Bacteria()
                    raza = temp_bacteria.random_raza()
                    resistencia = temp_bacteria.random_resistencia()
                    temp_bacteria.crear_bacteria(raza, resistencia)
                    temp_colonia.agregar_bacteria(temp_bacteria)
                m -= 1
                temp_colonia.set_Ambiente(ambiente_simulado)
                ambiente_simulado.agregar_colonia(temp_colonia)
                ambiente_simulado.posicion.append(temp_colonia.lugar)
        while o > 0:
            ambiente_simulado.crear_espacio(4)
            o -= 1
        self.exportar_csv(archivo, ambiente_simulado, p)                
        self.graficar_resultados(ambiente_simulado)

    
    
    def recolectar_datos(self,tiempo,ambiente):
        tiempos=0
        bacterias_vivas=0
        bacterias_resistente=0
        total_bacterias=0
        resistentes=0
        vivas=0
        for colonia in ambiente.colonias:
            for bacteria in colonia.bacterias:
                total_bacterias += 1
                if bacteria.estado==True:
                    vivas += 1
                    if bacteria.resistente==True:
                        resistentes += 1
        tiempos=tiempo
        bacterias_vivas=vivas
        bacterias_resistente=(resistentes/vivas*100)
        return [tiempos,bacterias_vivas,bacterias_resistente]

    def graficar_resultados(self, ambiente):
        # Ensure grilla is a numpy array
        grilla=self.crear_grillas(ambiente)

        # Define the colormap
        cmap = plt.cm.get_cmap('Set1', 5)
        fig, ax = plt.subplots(figsize=(6, 6))
        cax = ax.matshow(grilla, cmap=cmap)

        # Create legend elements
        legend_elements = [
            Patch(facecolor=cmap(1/5), label='Bacteria activa'),
            Patch(facecolor=cmap(2/5), label='Bacteria Muerta'),
            Patch(facecolor=cmap(3/5), label='Bacteria Resistente'),
            Patch(facecolor=cmap(4/5), label='Bacteria Biofilm'),
        ]
        ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.45, 1))

        # Set ticks
        ax.set_xticks(np.arange(0, 5, 1))
        ax.set_yticks(np.arange(0, 5, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(color='gray', linestyle='-', linewidth=0.5)

        # Annotate the cells with values
        for i in range(grilla.shape[0]):
            for j in range(grilla.shape[1]):
                val = grilla[i, j]
                if val > 0:
                    ax.text(j, i, int(val), va='center', ha='center', color='white')

        plt.title("Grilla 5x5")
        plt.tight_layout()
        plt.show()


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


if __name__ == "__main__":
    app = simulacion()
    app.run()

    
