import csv
import os
from datetime import datetime

# Creamos una clase padre llamada Usuario, que será la clase padre. 

class Usuario():
    def __init__(self, nombre, apellido, password, email, genero, edad): # Constructor de Usuario
        self.nombre = nombre  # Atributos de la clase Usuario
        self.apellido = apellido
        self.password = password
        self.email = email
        self.genero = genero
        self.edad = edad

# Creamos métodos para la clase Usuario.
# El primer método simula el registro de usuarios.         
    @classmethod # Decorador que nos permite tomar como argumento la clase Usuario. Con este se puede obtener el input del usuario y lo entrega al constructor.
    def registro_usuario(self, archivo): # Damos como parámetro el archico en el cuál serán registrados los usuarios. 
        with open(archivo, 'a') as archivo_csv: # EL indicador "a" pemitirá agrgar a los usuarios en un archivo.csv
            escribir = csv.writer(archivo_csv, delimiter = ',') # Creamos el objeto escribir para escribir nuestro usuario en un archivo.csv.
            os.system('cls')
            try: # Este try permite capturar el error TypeValue que se genera cuando la edad ingresada no es un número.
                nombre = input('Nombre: ') # Datos solicitados para el registro de usuarios. 
                apellido = input('Apellido: ')
                password = input('Password: ')
                email = input('Email: ')
                genero = input('Género: ')
                edad = int(input('Edad: '))
                escribir.writerow([nombre, apellido, password, email, genero, edad]) # Se ecribirá esta lista en un archivo.csv
                return self(nombre, apellido, password, email, genero, edad)# Indicamos que estos parámetros considerados.         
            except: # Capturamos el erros. 
              print('Error al ingresar datos') # Mensaje que se genera cuando se produce el error.
     
    @classmethod # Decorador que nos permite tomar como argumento la clase Usuario. Con este se puede obtener el input del usuario y lo entrega al constructor.
    def login_usuario(self, archivo): # Este método simulará un login, basándonos en los registros realizados. 
        with open(archivo) as login: # buscaremos los datos en el archivo csv de usuarios registrados. 
            self.nombre = input("Ingrese nombre de usuario: ")  # Datos solicitados para el login de usuarios.
            self.password = input("Ingrese contraseña: ")
            leer = csv.reader(login, delimiter=',') # Creamos la función leer para buscar en el archivo.
            for fila in leer:  #Este ciclo for busca al usuario mediante un recorrido. 
                if self.nombre and self.password in fila: # Si el usuario existe, se muestra el siguiente mensaje.
                    return "Bienvenid@" + " " + self.nombre + " " + "sus datos son: \n" + str(fila)
            return "Campos inválidos"

    @classmethod # Decorador que nos permite tomar como argumento la clase Usuario. Con este se puede obtener el input del usuario y lo entrega al constructor.
    def buscar_usuario(self, archivo): # Este método simulará un login, basándonos en los registros realizados. 
          with open(archivo) as archivo:
              self.nombre = input("Ingrese el nombre del usuario que busca: ")
              leer = csv.reader(archivo, delimiter=',') # Creamos la función leer para buscar en el archivo.
              for self.nombre in leer:
                  if self.nombre in leer:
                      return "Usuario encontrado"
              return "Usuario no existe"

# Creamos una clase hija llamada Administrador, que hereda atributos y métodos de la clase Usuario. 

class Administrador(Usuario):
    def __init__(self, nombre, apellido, password, email, genero, edad): # Constructor
        super().__init__(nombre, apellido, password, email, genero, edad) # Obtenemos los atributos mediante el método super().
    
    @classmethod 
    def registro_administrador(self): # Obtenemos la función "registro_usuario" de Usuario, mediante el método super().
        super().registro_usuario(archivo1)
        return "Usted ha sido registrado"

    @classmethod 
    def login_administrador(self): # Obtenemos la función "login_usuario" de Usuario, mediante el método super().
        return super().login_usuario(archivo1)
        

# Creamos una clase hija llamada Usuario_Unico, que hereda atributos y métodos de la clase Usuario. 

class Usuario_Unico(Usuario): 
    def __init__(self, nombre, apellido, password, email, genero, edad): # Constructor
        super().__init__(nombre, apellido, password, email, genero, edad) # Obtenemos los atributos mediante el método super().
 
    @classmethod 
    def registro_usuario_unico(self): # Obtenemos la función "registro_usuario" de Usuario, mediante el método super().
        super().registro_usuario(archivo2)
        

# Creamos una clase hija llamada Usuario_Registrado, que hereda atributos y métodos de la clase Usuario. 

class Usuario_Registrado(Usuario): 
    def __init__(self, nombre, apellido, password, email, genero, edad): # Constructor
        super().__init__(nombre, apellido, password, email, genero, edad) # Obtenemos los atributos mediante el método super().
    
    @classmethod 
    def login_usuario_registrado(self):
        super().login_usuario(archivo2) # Obtenemos la función "login_usuario" de Usuario, mediante el método super()
    

# Definimos los archivos en los cuales se registrarán los usuarios. 

archivo1 = os.path.join("data", "administradores.csv")
archivo2 = os.path.join("data", "usuarios_registrados.csv")


#Llamamos a las funciones implementadas en Administrador. 
print("Registro Administrador")
administrador1 = Administrador.registro_administrador()
print(administrador1)
print("-" * 90)
print("Ingreso de Administrador")
administrador1 = Administrador.login_administrador()
print("-" * 90)

#Llamamos a las funciones implementadas en Usuario_Unico. 
print("Registro de Usuario")
usuario_registrado1 = Usuario_Unico.registro_usuario_unico()
print(usuario_registrado1)
print("-" * 90)

# Llamamos a las funciones implementadas en Usuario_Registrado. 
print("Ingreso de Usuarios")
usuario_registrado1 = Usuario_Registrado.login_usuario_registrado() 
print(usuario_registrado1)

# Se crea una función de búsqueda de usuarios por nombre. 
try: # Controlamos con un error si no se entrega un argumento. 
    buscar = Usuario.buscar_usuario()  # Se da como argumento el archivo en el cual deseamos buscar al usuario. 
    print(buscar) 
except TypeError: # Si no se entrega como argumento el archivo en donde queremos buscar, se captura el error. 
    print("Debe indicar el archico en donde desea realizar la búsqueda.") # Mensaje de error. 




