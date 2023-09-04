import matplotlib.pyplot as plt
import numpy as np
#La siguiente es nuestra función para la creación de la lista de tuplas, aunque funcionara bien decidimos usar la tuya.
#def creacion_tuplas(archivo):
    #listatuplas=[]
    #with open(archivo, encoding='utf-8') as f:
      #lineas=f.readlines()
    #numero=len(lineas)
    #cont1=0
    #cont2=0
    #for k in range(numero-1):
       
       
       #if "data" in lineas[k]:
          #cont1+=k
       #if "SPECS" in lineas[k]:
          #cont2+=k
       
    #for i in range(cont1,cont2):
       #ejemplo=lineas[i].strip()
       #ejemplo2=ejemplo.split(" ")
       #tupla=(float(ejemplo2[0]),float(ejemplo2[1]))
       #listatuplas.append(tupla)
    #return listatuplas
    
def func_archivoyml_tuplas(ruta_yml: str) -> list:
    '''
     Lee los archivos yml y devuelve la lista de tuplas
    '''
    f = open(ruta_yml)
    texto_archivo = f.read() #text_archivo es un string de todo lo que contiene el archivo
    f.close()

    # A continuación, note que el texto lo separamos por data: |\n, así como en \nSPECS y - type.
    # Si bien no todos los archivos tienen estos dos últimos strings de terminación, se pueden incluir
    # para buscar el caso más generla
    lista_unprocessed = texto_archivo.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
    
    # Acá si gustan pueden darle un print a lista_unprocessed para ver el resultado
    lista_final = []

    for k in lista_unprocessed:
        texto = k.split(' ')
        texto[0] = float(texto[0])
        texto[1] = float(texto[1])
        lista_final.append(tuple(texto))
   
    return lista_final

         
    

ruta_archivo_AO="/Users/simon/OneDrive/Documentos/3er semestre/MCI/Notas-del-profe/MetodosComputacionales202320-1/Materiales/Adhesivos/NOA138.1"
ruta_archivo_PC="/Users/simon/OneDrive/Documentos/3er semestre/MCI/Notas-del-profe/MetodosComputacionales202320-1/Materiales/Plasticos_Comerciales/French.yml"
ruta_carpeta_prueba="/Users/simon/OneDrive/Documentos/3er semestre/MCI/Notas-del-profe/MetodosComputacionales202320-1/Materiales/Plasticos_Comerciales/Graf_Kapton.png"
a=(func_archivoyml_tuplas(ruta_archivo_PC))
b=(func_archivoyml_tuplas(ruta_archivo_AO))
atitul="Kapton"
btitul="NOA138"


def Graficar_materiales (lista, titul, ruta_destino):
    
   x=[]
   y=[]
   for i in range (len(lista)-1):
      x.append(lista[i][0])
      y.append(lista[i][1])
   prom=round(np.mean(y),2)
   desv=round(np.std(y),2)
   titulo=titul+" Promedio: "+str(prom)+" Desv estándar: "+str(desv)
   plt.scatter(x,y)
   plt.title(titulo)
   plt.xlabel("lamda")
   plt.ylabel("n")
   plt.savefig(ruta_destino)
   plt.show()

print(Graficar_materiales(a,atitul,ruta_carpeta_prueba))
#print(Graficar_materiales(b,btitul))

