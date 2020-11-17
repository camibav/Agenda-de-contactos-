# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:44:53 2020

@author: keita
"""
import os # esta dise;ado para manejar archivos
CARPETA='Contactos/' # carpeta donde se guardan los contactos
EXTENSION='.txt' # extension de los archivos
ind={'colombia':'+57','argentina':'+54','chile':'+56','brasil':'+55','bolivia':'+591','ecuador':'+593','peru':'+51','venezuela':'+58','uruguay':'+598','paraguay':'595'} #indicativos del numero telefonico
class Contactos:
    def __init__(self,nombre,telefono,categoria,pais):
        self.nombre=nombre
        self.telefono=telefono
        self.categoria=categoria
        self.pais=pais

def app():
    crear_directorio()# revisa y crea una carpeta
    mostrar_menu()
    preguntar= True
    
    while preguntar:
       
        opcion=int(input('Seleccione una opcion: \r\n'))
        if opcion== 1:
            agregar_contacto()
            preguntar=False
        elif opcion==2:
             editar_contacto()
             preguntar=False
        elif opcion==3:
             mostrar_contactos()
             preguntar=False
        elif opcion==4:
             buscar_contacto()
             preguntar=False
        elif opcion== 5:
             borrar_contacto()
             preguntar=False
        elif opcion==6:
            print('Gracias por usar la app! ')
            preguntar=False
        else:
            print("¡Error! elija una opcion valida ")
def  borrar_contacto():
    nombre= input('Digite el contacto que desea eliminar:\r\n')
    try:
        os.remove(CARPETA+nombre+EXTENSION)
    except:
        print(f'El contacto {nombre.title()} no existe ')
    app()
        
        
def buscar_contacto():
    nombre=input("Seleccione el contacto que desea buscar: \r\n")
    try:
        with open(CARPETA +nombre+EXTENSION) as contacto:
             print(f'\r\n Informacion del contacto {nombre} : \r\n')
             for linea in contacto:
                 print(linea.rstrip()) 
        
    except IOError:
        print(f'El contacto {nombre} no existe ')
        print (IOError)
    app()
        
    
def mostrar_contactos():
    archivos= os.listdir(CARPETA)  #nos permite listar los archivos
    archi_txt= [i for i in archivos if i.endswith(EXTENSION)] # recorre el iterador solo si el archivo termina en txt
    for archivo in archi_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip() + '\r\n') #imprime los contenidos y quita el salto de linea 
                #print('\r\n')
    app()
def editar_contacto(): 
    nombre_anterior=input('Nombre del contacto que desea editar: \r\n')
    existe= existe_contacto(nombre_anterior.title())# comprobar si existe el contacto
    if existe:
        
        with open(CARPETA + nombre_anterior.title()+EXTENSION, 'w') as archivo:# abre el archivo si existe
             nombre_contacto=input('Agrega el nuevo nombre del contacto: \r\n ')   
             telefono_contacto=input('Agrega el nuevo telefono del contacto: \r\n')
             categoria_contacto=input('Agrega la nuevo categoria del contacto \r\n')
             pais_contacto=input("Agrega el nuevo pais del contacto:\r\n")
             contacto= Contactos(nombre_contacto,telefono_contacto,categoria_contacto,pais_contacto)# uso la clase Contactos
             archivo.write('Nombre: ' + contacto.nombre.title() +'\r\n'  )# se escribe el nombre del contacto dentro del archivo .txt
             archivo.write('Categoria: '+ contacto.categoria.title() +'\r\n')
           
             if contacto.pais == 'argentina':
                 p=ind['argentina']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'brasil':
                 p=ind['brasil']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )    
             elif contacto.pais  == 'bolivia':
                 p=ind['bolivia']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'colombia':
                 p=ind['colombia']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'chile':
                 p=ind['chile']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'peru':
                 p=ind['peru']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'paraguay':
                 p=ind['paraguay']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'ecuador':
                 p=ind['ecuador']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif pais_contacto == 'uruguay':
                 p=ind['uruguay']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' ) 
             elif pais_contacto == 'venezuela':
                 p=ind['venezuela']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             else:
                 print('El pais ingresado no es valido ')
                 app()
             archivo.close()
             
             
             os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto.title() + EXTENSION) #renombramos el archivo y el segunfo valor de rename(luego de la coma)sera su nuevo nombre
             print(f" \r\n El contacto {nombre_contacto.title()} se edito con exito \r\n" )  
             app()
    else:
        print(f"El contacto {nombre_anterior.title()} no existe")
    app()
def agregar_contacto(): # funcion para agregar los contactos
    
    print("Escribe los datos del nuevo contacto: " )
    nombre_contacto=input('Nombre del contacto: \r\n')
    existe= existe_contacto(nombre_contacto)# comprobar si existe el contacto
    if not existe:
        telefono_contacto=input('Telefono del contacto: \r\n')
        categoria_contacto=input('Categoria del contacto \r\n')
        pais_contacto=input("Pais del contacto:\r\n")
        
        contacto= Contactos(nombre_contacto,telefono_contacto,categoria_contacto,pais_contacto)# uso la clase Contactos
    
        with open(CARPETA + contacto.nombre.title() +EXTENSION, 'w') as archivo: # se crea un archivo .txt con el nombre del contacto en la carpeta 
             archivo.write('Nombre: ' + contacto.nombre.title() +'\r\n' )# se escribe el nombre del contacto dentro del archivo .txt
            
             archivo.write('Categoria: '+ contacto.categoria.title() +'\r\n')
             if contacto.pais == 'argentina':
                 p=ind['argentina']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'brasil':
                 p=ind['brasil']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )    
             elif contacto.pais  == 'bolivia':
                 p=ind['bolivia']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'colombia':
                 p=ind['colombia']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'chile':
                 p=ind['chile']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'peru':
                 p=ind['peru']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'paraguay':
                 p=ind['paraguay']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif contacto.pais  == 'ecuador':
                 p=ind['ecuador']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             elif pais_contacto == 'uruguay':
                 p=ind['uruguay']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' ) 
             elif pais_contacto == 'venezuela':
                 p=ind['venezuela']
                 archivo.write('Telefono: '+ p +' '+ contacto.telefono   +'\r\n' )
             else:
                 print('El pais ingresado no es valido ')
                 app()
             app()
             
             print (f"\r\n Contacto {nombre_contacto.title()} se creo correctamente \r\n")
    else:
         print(f"El contacto { nombre_contacto.title()} ya existe ")
         
def mostrar_menu():
    print("Bienvenido a su app de contactos ")
    print('en el menu se encuentran las acciones que puede realizar con esta app \r\n')
    print('1) Agregar contacto ') 
    print('2) Editar contacto ')
    print('3) Ver contacto ')
    print ('4) Buscar contacto')
    print('5) Borrar contacto ')
    print('6) cerrar la app ')
    
def crear_directorio():
    if not os.path.exists(CARPETA):# comprueba si una carpeta existe
        os.makedirs(CARPETA)# crea la carpeta
def existe_contacto(nombre):
    return  os.path.isfile(CARPETA + nombre +EXTENSION)# comprobar si existe el contacto
app()
        


    
    
    
    
    
    
