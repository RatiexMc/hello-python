### Comentarios ###
# Este es un comentario en una línea
"""
Esto es un comentario 
en varias líneas
"""
'''
Esto también es un comentario
en varias líneas
'''
print("Hola Mundo") 
print('Hola Python')
#Consultar el tipo de dato
print(type(10)) # int
print(type(3.14)) # float
print(type(True)) # Booleano
print(type(1 + 3j))# complex number
print(type("Hola, que tal")) # string
print(type([1,2,3])) # list
print(type({"Nombre":"Junior"})) # Dictionary
print(type({9.8,3.14,2.7})) # Set
print(type((9.8,3.14,2.7))) # Tuple
print(type(print("Mi cadena de texto"))) # Tipo 'NoneType' ¡Humor!
### Variables ###
print("VARIABLES")
my_string_variable = 'My String Variable' # Variable String
print(my_string_variable)
my_int_variable = 5 # Variable Int
print(my_int_variable)
my_int_to_str_variable = str(my_int_variable)#Una variable que inicialmente era entera, la transformó a String
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) 
my_bool_variable = False # Variable bool
print(my_bool_variable)
#Variables en una sola línea ¡Cuidado con abusar esta sintaxis!
name, surname, alias, age = "MiNombre","MiApellido","MiApodo",22
print("Me llamo: ",name,surname,". Mi edad es:",age,". Y mi alias es:",alias)
#Pide datos en la consola y imprime datos en la consola
"""
Está en comentario, para que no me pidiera cada rato mi nombre y edad cuando iba realizando dicho curso
name = input("¿Como te llamas? ")
age = input("¿Cual es tu edad? ")
"""
print (name)
print (age)
#Cambiamos su tipo debido a que no está fuertemente tipado, es tipado dinámico     
name = 35
age = "MiNombre"
print (name)
print (age)
#¿¿Forzamos el tipo??
address: str = "Mi dirección"
address = 32
address = True
address = 1.2
print(type(address))
#Concatenación de Variables en un Print
print(my_string_variable, str(my_int_variable) ,my_bool_variable) 
print("Este es el valor de:",my_bool_variable)
#Algunas funciones del sistema
print(len(my_string_variable)) # Contar caracteres 18 
### Operadores Aritméticos ###
print("OPERADORES ARITMÉTICOS")
print(3+4) # Adicción
print(3-4) # Sustracción
print(3*4) # Multiplicación
print(3/4) # División
print(10%3) # Modulos/Resto
print(10//3) # División Entera
print(2**3) # Exponentes 2x2x2=8
print(2**3+3-7/1//4)#Imprimir Operaciones conjuntas
print("Hola "+" Python "+" ¿Que tal? ")# + se usa para concatenar 
print("Hola " + str(5))#Concatenamos un valor con un string 
print("Hola " * 5) #Multiplicamos el texto "Hola" y aparece 5 veces
print("Chau "*(2**3))# Otro ejemplo apareciendo 8 veces debido a 2x2x2=8
my_float = 2.5 * 2
print("Ey " * int(my_float)) #Imprime 5 veces Ey, debido a convertir int la variable de operaciones my_float
### Operadores Comparativos ###
print("OPERADORES COMPARATIVOS")
#Da resultado True o False
print(3>4)
print(3<4)
print(3>=4)
print(3<=4)
print(3==4)
print(3!=4)
print("Hola">"Python")
print("Hola"<"Python")
print("aaaa">="AAAA")
print("aaaa">="abaa")#Ordenación alfabética por ASCII
print(len("aaaa")>=len("abaa"))#Cuenta caracteres
print("Hola">="Bola")
print("Hola">="Zola")
print("Hola"<="Python")
print("Hola"=="Hola")
print("Hola"!="Python")
### Operadores Lógicos ###
print("OPERADORES LÓGICOS")
print(3>4 and "Hola">"Python")#&&
print(3>4 or "Hola">"Python")#||
print(3<4 and "Hola"<"Python")
print(3<4 or "Hola"<"Python")
print(3<4 or "Hola">"Python")
print(3<4 or ("Hola">"Python" and 4==4))
print(not(3>4))#!= NoFalso es verdadero, Estamos negando que es falso, por tanto es verdadero
### Strings ###
print("STRINGS")
my_string = "Mi String"
my_other_string = 'Mi otro String'
print(len(my_string))
print(len(my_other_string))
print(my_string+" "+my_other_string)
my_new_line_string = "Este es un String \n Con salto de Línea"
print(my_new_line_string)
my_tab_string = "\tEste es un String con Tabulación"
print(my_tab_string)
my_scape_string ="\tEste es un string \n Escapado "
print(my_scape_string)
### Formateo ###
# %s String %d Entero %f Floating
name, surname, age = "Junior","OVS", 22
print("Mi nombre es " + name + " " + surname + " y mi edad es " +str(age))
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es {name} {surname} y mi edad es {age}")
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
### Desempaquetado de caracteres ###
language = "python"
a, b, c, d, e, f, = language
print(a)
print(e)
### División ###
print("Division de String")
language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]#Desde 1 hasta el Final
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[0:6:2]# Pilla el rango y luego evita cada cierto rango yCaracter 2, 4, 6
print(language_slice)
#Reverse
reversed_language = language[::-1]
print(reversed_language)
#Funciones
print("FUNCIONES")
print(language.capitalize()) #Primeraletra en Mayuscula
print(language.upper())#Mayuscula
print(language.count("t"))#Contar cuantas T
print(language.isnumeric())#Pregunta si es númerica
print("1".isnumeric())
print(language.lower())#Minuscula
print(language.upper().isupper())#Comprueba si es minuscula o mayuscula upper/lower
print(language.startswith("Py"))# python empieza con Py? False
print(language.startswith("py"))# python empieza con py? Verdadero
print("Py" == "py") # True
### Listas ###
# Array no es lo mismo que Lista
print("LISTAS")
print(list([1,2,3,4]))
print([1,2,3,4])
my_list = list()
my_other_list = []
print(len(my_list))
my_list = [35,24,62,52,30,30,17]
print(my_list)
print(len(my_list))
my_other_list = [35, 1.73, "Junior", "OVS"]
print(type(my_list))
print(my_other_list)
print(type(my_other_list))
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
print("Indice de OVS")
print(my_other_list.index("OVS"))
print(my_list.count(30))
age, height, name, surname = my_other_list
print(name)
name, height, age, surname = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3],
print(age)
print(my_list + my_other_list)#Concatenar Lista
print(my_other_list + my_list)
print("Operaciones en Lista")
my_other_list.append("JuniorOVSDev")#Insertar al final
print(my_other_list)
my_other_list.insert(1,"Rojo")#Insertar en la posicion 1, meter el valor Rojo
print(my_other_list) 
my_other_list[1] = "Azul"#Modifica el valor de la posicion 1
print(my_other_list)
my_other_list.remove("Azul")#Eliminar Azul de la lista
print(my_other_list) 
print("Vemos nuestra Lista")
print(my_list)
my_list.remove(30)#Me elimino el primer elemento "30"
print(my_list)
print("Mi ->POP<- elimina el ultimo elemento")
print(my_list.pop())#Se cargó al último elemento, es decir el 17
print(my_list)
print("Podemos guardar el pop creando una variable")
my_pop_element = my_list.pop(2)#Eliminamos al POP 62 que está en el índice 2
print(my_pop_element)
print(my_list)
del my_list [2] #Podemos eliminar sin retorno
print(my_list)
print("Hacemos la copia de lista")
my_new_list = my_list.copy()#Llama a copy
my_list.clear() #Limpia la lista
print(my_list)
print(my_new_list)
my_new_list.reverse()
print(my_new_list)
my_new_list.sort()#Ordena la palabra de menor a mayor con enteros en este caso
print(my_new_list)
print(my_new_list[1:3])
my_list = "Hola Python"
print(my_list)
print(type(my_list))
my_list = list("Hola Python")
my_list = ["Hola Python"]
print(my_list)
print(type(my_list))
### TUPLES ###
print("Tuples")
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (22, 1.73,"Junior","OVS","Junior")
my_other_tuple =(35,60,30)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError
print(my_tuple.count("Junior"))
print(my_tuple.index("OVS"))#Nos indica el indice de OVS
print(my_tuple.index("Junior"))#Se queda con el primer indice
#Diferencia de Lista podemos borrar, insertar, etc. y 
# Tuplas es inmutable, donde guardas y se queda conjunto cerrado 
# y inicializado. Tupla no se puede modificar
#my_tuple[1] = 1.80 #'tuple' object does not supoort item assignment
print(my_tuple + my_other_tuple) #Concatenar Tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])
print("¿Modificaciones de Tuples?")
print(my_tuple)
my_tuple=list(my_tuple)
print(type(my_tuple))
my_tuple[4] = "JuniorOVSDev"
my_tuple.insert(1, "Azul")
my_tuple =tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion
del my_tuple 
#print(my_tuple) # Name error: name 'my_tuple' is not defined
### SETS ###
print("SETS")
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))#Inicialmente es un diccionario
my_other_set = {"Junior","OVS",22}
print(type(my_other_set))
print(len(my_other_set))
my_other_set.add("JuniorOVS")
print(my_other_set) # Un set no es una estructura ordenada
my_other_set.add("JuniorOVS") # Un set no admite repetidos, por tanto no accedemos a su índice
print(my_other_set)
print("Junior" in my_other_set) # Sintaxis para comprobar si existe en my_other_set
print("Juniur" in my_other_set)
my_other_set.remove("Junior")
print(my_other_set)
my_other_set.clear()
print(len(my_other_set))
del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined
my_set= {"Junior","OVS",22}
my_list= list(my_set)
print(my_list[0])
my_other_set = {"Java","JavaScript","Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
#Sets no acepta repetido
print(my_new_set.union(my_new_set))
print(my_new_set.union(my_new_set).union(my_set))
print(my_new_set.union(my_new_set).union(my_set).union({"Git","HTML"}))
print(my_new_set.difference(my_set))
### Diccionarios ###
# Almacena clave - valor
my_dict = dict()
my_other_dict ={}
print(type(my_dict))
print(type(my_other_dict))
my_other_dict = {"Nombre":"Junior","Apellido:":"OVS","Edad:":22, 1:"Python"}
my_dict = {
    "Nombre":"Junior",
    "Apellido":"OVS",
    "Edad":22, 
    "Lenguajes":{"Python","Java","HTML"},
    1:1.73
    }
print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))#5 porque hay 5 claves
print(my_dict["Nombre"])
my_dict["Nombre"] = "Andrea" #Reemplazar
print(my_dict["Nombre"])
print(my_dict[1])
my_dict["Calle"] = "Calle JuniorOVS"#Añadir
print(my_dict)
del my_dict["Calle"]#Eliminar(No se puede recuperar)
print(my_dict)
print("Junior" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])
print(my_dict.items())#Listados
print(my_dict.keys())#Keys
print(my_dict.values())#Valores
#Crear un diccionario nuevo sin 
my_list = ["Nombre",1,"Piso"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre",1, "Piso"))#Lo correcto
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
#my_new_dict = dict.fromkeys(my_dict,("Junior","OVS"))#Metimos Junior, OVS a todos los elementos
my_new_dict = dict.fromkeys(my_dict,"Junior")
print("Cada caso")
print(my_new_dict)
my_values = my_new_dict.values()
print(type(my_values))#Tipo de datos diccionario de valores
print(my_new_dict.values())
print(list(my_new_dict.values()))
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
### CONDICIONALES ###
print("CONDICIONALES")










