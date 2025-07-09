import random
import gi 
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch  
import csv
import re
import pandas as pd

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
        else:
            return
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
        else:
            return
    #si pierde energia se muere
    def morir(self):
        if self.energia<=100 and self.estado==True:
            self.estado=False
            return           
        if self.estado==True:
            return
        else:
            return
    def morir_antibiotico(self):
        if self.resistente==True:
            return
        else:
            muerte=random.randint(1,5)
            if muerte<=2:
                self.estado=False

#clase ambiente
class Ambiente():
    def __init__(self):
        self.grilla=np.zeros((5,5))
        self.factor_ambiental=None
        self.posicion=[]
        self.colonias=[]

    def alimentar(self,N):
        if isinstance(N,int):
            self.nutrientes+=N

    def agregar_colonia(self,Col):
        if isinstance(Col,Colonia):
            self.colonias.append(Col)     
    #crea un random para agregar nutrientes
    def difundir_nutrientes(self):
        nuevos_nutrientes=random.randint(100,500)
        nuevos_nutrientes=nuevos_nutrientes//len(self.colonias)
        for colonia in self.colonias:
            colonia.nutrientes+=nuevos_nutrientes
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
        self.lugar=[1,1,1]
        self.tipo=1
        self.nutrientes=random.randint(100,1000)

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
        nueva_colonia.set_tipo(self.tipo)
        if nueva_colonia.reporte_estado==0:
            return
        else:
            return nueva_colonia
    #comprobacion de movimiento de la colonia en el ambiente
    def paso(self):
        if self.lugar[2]!=1:
            return
        else:
            estado = self.reporte_estado()  # Guardar el resultado
            for i in range(len(self.bacterias)):
                self.bacterias[i].energia -= 10
                self.bacterias[i].morir()
                self.bacterias[i].mutar()
                self.bacterias[i].Alimentar(self.nutrientes,self.nutrientes//len(self.bacterias))
            if estado == 0:
                self.lugar[2] = 2                     
            if len(self.bacterias) > 0:
                mov = random.randint(1, 4)
                x = self.lugar[0]
                y = self.lugar[1]   
                if 0 < x < 4 and 0 < y < 4: 
                    if (self.ambiente.grilla[x + 1][y] == 4 or
                        self.ambiente.grilla[x - 1][y] == 4 or
                        self.ambiente.grilla[x][y + 1] == 4 or
                        self.ambiente.grilla[x][y - 1] == 4):
                        for Bacteria in self.bacterias:
                            Bacteria.mutar() 
                            Bacteria.morir_antibiotico()            
                NC = self.crear_colonia()
                if mov == 1 and x < 4:
                    nuevo_lugar=self.lugar
                    nuevo_lugar[0]=nuevo_lugar[0]+1
                    NC.set_lugar(nuevo_lugar)
                elif mov == 2 and y < 4:
                    nuevo_lugar=self.lugar
                    nuevo_lugar[1]=nuevo_lugar[1]+1
                    NC.set_lugar(nuevo_lugar)  
                elif mov == 3 and x > 0:
                    nuevo_lugar=self.lugar
                    nuevo_lugar[1]=nuevo_lugar[0]-1
                    NC.set_lugar(nuevo_lugar) 
                elif mov == 4 and y > 0:
                    nuevo_lugar=self.lugar
                    nuevo_lugar[1]=nuevo_lugar[1]-1
                    NC.set_lugar(nuevo_lugar)
                else:
                    for bacteria in self.bacterias:
                        nueva=bacteria.dividirse()
                        if nueva==None:
                            return
                        else:
                            self.bacterias.append(nueva)
                
                self.ambiente.posicion.append(NC.lugar)
                self.ambiente.colonias.append(NC)
                self.ambiente.difundir_nutrientes()


    #reporte de si existen bacterias vivas o estan muertas en la casilla             
    def reporte_estado(self):
        suma_estados=0
        total_bacterias = 0
        resiste=0
        for bacteria in self.bacterias:
            if bacteria.estado==True:
                suma_estados += 1
            if bacteria.resistente==True:
                resiste+=1
            total_bacterias+=1
        if resiste==suma_estados:
            self.tipo=3
        if suma_estados==0:
            self.tipo=2            
        return suma_estados
    
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
            x=ambiente.posicion[i][0]
            y=ambiente.posicion[i][1]
            k=ambiente.posicion[i][2]
            if grilla[x,y]==0:
                grilla[x,y]=k
        return grilla

    def do_activate(self):
        self.window = Gtk.ApplicationWindow(application=self)
        self.window.set_title("Lab de Bacterias simuladas")
        self.window.set_default_size(720, 480)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window.set_child(box)

        self.Colonias_iniciales= Gtk.Entry()
        self.Colonias_iniciales.set_text("Ingrese Colonias")
        box.append(self.Colonias_iniciales)

        self.Bacterias_iniciales = Gtk.Entry()
        self.Bacterias_iniciales.set_text("Ingrese Bacterias por colonia")
        box.append(self.Bacterias_iniciales)
        
        self.Antibioticos=Gtk.Entry()
        self.Antibioticos.set_text("Ingrese cantidad de Antibioticos")
        box.append(self.Antibioticos)

        self.Cantidad_de_pasos=Gtk.Entry()
        self.Cantidad_de_pasos.set_text("Ingrese Cantidad de pasos que va hacer")
        box.append(self.Cantidad_de_pasos)

        self.Boton_Iniciar = Gtk.Button(label="Iniciar")
        self.Boton_Iniciar.connect("clicked", self.Iniciar_clicked)
        box.append(self.Boton_Iniciar)

        self.window.show()

    def exportar_csv(self, archivo, ambiente, pasos):
        n=pasos
        paso=1
        Total_datos=[]
        with open(archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(['id_bacteria', 'raza', 'energia', 'es_resistente', 'esta_viva','Cuadrilla','Tiempo(en pasos)'])
            while n>0: 
                for colonia in ambiente.colonias:
                    for Bacteria in colonia.bacterias:
                        escritor.writerow([
                            Bacteria.id,
                            Bacteria.raza,
                            Bacteria.energia,
                            Bacteria.resistente,
                            Bacteria.estado,
                            colonia.lugar,
                            paso
                        ])
                    datos_colonia=self.recolectar_datos(paso, ambiente)
                    Total_datos.append(datos_colonia)
                    colonia.paso()                                                                                                                                                                                                                                         
                paso+=1
                n-=1
        return Total_datos

        
    
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
        grilla=self.crear_grillas(ambiente_simulado)
        datos=self.exportar_csv(archivo,ambiente_simulado,p)
        ambiente_simulado.grilla=grilla
        print(datos)
        self.graficar_crecimiento_bacterias(datos,p)
        self.graficar_Resistencia

    
    
    def recolectar_datos(self,tiempo,ambiente):
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
        bacterias_vivas=vivas
        if vivas!=0:
            bacterias_resistente=(resistentes)
        else:
            bacterias_resistente=0
        return [tiempo,bacterias_vivas,bacterias_resistente]

    def graficar_crecimiento_bacterias(self, matriz_datos,p):
        pt=p
        n=1
        columna_tiempo=[]
        columna_bacterias=[]
        while pt>0:
            columna_tiempo.append(n)
            n+=1
            pt-=1
        for list in matriz_datos:
            bacteriasT=0
            while list[0]==n:
                bacteriasT+=list[1]
            columna_bacterias.append(bacteriasT)

        plt.figure(figsize=(10, 4))
        plt.plot(columna_bacterias,columna_tiempo, label='c')
        plt.title('Bacterias vs tiempo')
        plt.xlabel('Bacterias')
        plt.ylabel('Pasos')
        plt.legend()
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def graficar_Resistencia(self,matriz_datos,p):
        pt=p
        n=1
        columna_tiempo=[]
        columna_bacterias=[]
        columna_resistencia=[]
        while pt>0:
            columna_tiempo.append(n)
            n+=1
            pt-=1
        for list in matriz_datos:
            bacteriasT=0
            bacteriasR=0
            while list[0]==n:
                bacteriasT+=list[1]
            while list[0]==n:
                resistentens+=list[2]
            columna_porcentaje.append((bacteriasR//bacteriasT)*100)


        plt.figure(figsize=(10, 4))
        plt.plot(columna_porcentaje,columna_tiempo, label='c')
        plt.title('porcentaje de resistencia vs tiempo')
        plt.xlabel('Bacterias')
        plt.ylabel('Pasos')
        plt.legend()
        plt.tight_layout()
        plt.grid(True)
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

    
