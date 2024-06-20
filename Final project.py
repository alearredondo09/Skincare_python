#Importamos todos los strings de información desde nuestro archivo strings.py
#También importamos la libreria os para poder identificar el sistema en el que se ejecuta el código
from strings import skincare, acne, rosacea, hidratacion, exfoliacion, rejuvenecimiento, cuerpo, cabello
import os

'''LISTAS'''
#Esta lista es para saber si un string es un dato númerico o no
digitos=["1","2","3","4","5","6","7","8","9","0","."]
#Las siguientes listas son las opciones disponibles para cada pregunta en el código
opciones_si_no=["si","no"]
opciones_main=["skincare", "cuidado del cabello"]
opciones_skincare=["cara","cuerpo","regresar","salir"]
opciones_cara=["acné","rosácea","hidratación","exfoliación","rejuvenecimiento","regresar","salir"]
opciones_hidratacion=["base agua","serúm","crema"]
opciones_exfoliacion=["grasa","mixta","seca","sensible"]
opciones_cuerpo=["higiene personal","exfoliación","hidratación","protección solar","cuidado de las uñas",
"cuidado de los pies","depilación","nutrición y ejercicio","descanso adecuado"]
opciones_cabello=["rizado","ondulado","lacio"]

#Para facilitar el acceso, guardamos todas estas listas en una matriz
matriz_validacion=[opciones_si_no,opciones_main,opciones_skincare,opciones_cara,opciones_hidratacion,
opciones_exfoliacion,opciones_cuerpo,opciones_cabello]

'''FUNCIONES'''
#Esperar a que el usuario conteste el input, sin importar lo que ingrese
def inputUsuario():
    input("Pulse enter para continuar\n\n>>> ")

#Limpiar pantalla
def limpiar_pantalla():
    #Sistema Mac o Linux
    if os.name == "posix":
        os.system("clear")
    #Sistema Windows
    else:
        os.system("cls")

#Función para validar si la opcion ingresada en un input es valida o no
def validarOpcion(opcion, lista):
    #Verifica si la opcion está en la lista de opciones
    if opcion.lower() in lista:
        #Busca la ubicación de la opción para ocuparla después en el código
        index=lista.index(opcion.lower())
        return True, index
    else:
        return False, 0

#Función del menú de cara
def opcion_cara():
    print("¿Sobre qué quieres saber?\n")
    #Este formato de ciclo pide un input hasta que sea valido
    #Ciclo Cara
    while True:
        print("Las opciones son:\n-acné\n-rosácea\n-hidratación\n-exfoliación\n-rejuvenecimiento\n-regresar\n-salir")
        opcion=input(">>> ")
        limpiar_pantalla()
        
        #Guarda la validez y el indice de la opcion dada
        validacion=validarOpcion(opcion, matriz_validacion[3])

        #Si no es valido, simplemente se volverá a pedir la opcion
        if validacion[0]:
            #Caso acné
            if validacion[1]==0:
                #Da informacion del acné
                print(acne[0])
                print("\n¿Quieres saber sobre tratamientos para el acné?\n")
                #Ciclo acné
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Da información extra
                            print(acne[1])
                            inputUsuario()
                        limpiar_pantalla()
                        break
            #Caso rosácea
            elif validacion[1]==1:
                #Da informacion de la rosácea
                print(rosacea[0])
                print("\n¿Quieres saber sobre tratamientos para la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Da informacion extra de la rosácea
                            print(rosacea[1])
                        break
                print("\n¿Quieres saber sobre factores de riesgo de la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Vuelve a dar más informacion extra
                            print(rosacea[2])
                        break
            #Caso hidratación
            elif validacion[1]==2:
                #Da informacion de la hidratación
                print(hidratacion[0])
                print("¿Te gustaría saber un método de hidratación?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print("¿De cuál te gustaría saber más a detalle?")
                            while True:
                                print("Las opciones son:\n-base agua\n-serúm\n-crema")
                                opcion=input(">>> ")
                                limpiar_pantalla()
                                
                                validacion=validarOpcion(opcion, matriz_validacion[4])

                                if validacion[0]:
                                    #Opción base agua
                                    if validacion[1]==0:
                                        print(hidratacion[1])
                                    #Opción serúm
                                    elif validacion[1]==1:
                                        print(hidratacion[2])
                                    #Opción crema
                                    elif validacion[1]==2:
                                        print(hidratacion[3])
                                    break
                        break
            #Caso exfoliación
            elif validacion[1]==3:
                #Da informacion de la exfoliación
                print(exfoliacion[0])
                print("¿Qué tipo de piel tienes?")
                while True:
                    print("Las opciones son:\n-grasa\n-mixta\n-seca\n-sensible")
                    opcion=input(">>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[5])

                    if validacion[0]:
                        #Guarda el tipo de piel en una variable para usarlo después
                        tipo_cara=validacion[1]
                        #Opción grasa
                        if validacion[1]==0:
                            print(exfoliacion[1])
                        #Opción mixta
                        elif validacion[1]==1:
                            print(exfoliacion[2])
                        #Opción seca
                        elif validacion[1]==2:
                            print(exfoliacion[3])
                        #Opción sensible
                        elif validacion[1]==3:
                            print(exfoliacion[4])
                        break
                print("¿Quieres conocer un tratamiento para tú tipo de piel?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        #Aquí se usa de nuevo el tipo de piel, pero ya está guardada
                        #Opción grasa
                        if tipo_cara==0:
                            print(exfoliacion[5][0])
                        #Opción mixta
                        elif tipo_cara==1:
                            print(exfoliacion[5][1])
                        #Opción seca
                        elif tipo_cara==2:
                            print(exfoliacion[5][2])
                        #Opción sensible
                        elif tipo_cara==3:
                            print(exfoliacion[5][3])
                        break
            #Caso rejuvenecimiento
            elif validacion[1]==4:
                #Da informacion de la rejuvenecimiento
                print(rejuvenecimiento[0])
                print("¿Desea conocer datos útiles sobre el rejuvenecimiento de la piel?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        #Da información extra del rejuvenecimiento
                        print(rejuvenecimiento[1])
                        print("¿Te gustaría saber sobre procedimientos de rejuvenecimiento?")
                        while True:
                            opcion=input("Debes contestar con si o no\n>>> ")
                            limpiar_pantalla()

                            validacion=validarOpcion(opcion, matriz_validacion[0])

                            if validacion[0]:
                                #Vuelve a dar información extra
                                print(rejuvenecimiento[2])
                                break
                        break
            #Caso regresar
            elif validacion[1]==5:
                opcion_skincare()
            #Si la opcion fue SALIR, el programa no vuelve a llamar la función anterior y llega directamente al menú de salida
            #Termina el ciclo de Cara
            break

#Función del menú de cuerpo
def opcion_cuerpo():
    #Da información general del cuidado del cuerpo, así cómo una lista de practicas para cuidarse
    print(cuerpo[0])
    print("¿Sobre cuál quieres saber?")
    while True:
        opcion=input("Las prácticas son:\n-Higiene Personal\n-Exfoliación\n"
        "-Hidratación\n-Protección Solar\n-Cuidado de las uñas\n-Cuidado de los pies\n"
        "-Depilación\n-Nutrición y ejercicio\n-Descanso adecuado\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[6])

        if validacion[0]:
            #Opción Higiene personal
            if validacion[1]==0:
                print(cuerpo[1])
            #Opción Exfoliación
            elif validacion[1]==1:
                print(cuerpo[2])
            #Opción Hidratación
            elif validacion[1]==2:
                print(cuerpo[3])
            #Opción Protección Solar
            elif validacion[1]==3:
                print(cuerpo[4])
            #Opción Cuidado de las uñas
            elif validacion[1]==4:
                print(cuerpo[5])
            #Opción Cuidado de los pies
            elif validacion[1]==5:
                print(cuerpo[6])
            #Opción Depilación
            elif validacion[1]==6:
                print(cuerpo[7])
            #Opción Nutrición y ejercicio
            elif validacion[1]==7:
                print(cuerpo[8])
            #Opción Descanso adecuado
            elif validacion[1]==8:
                print(cuerpo[9])
            break

#Función del menú de Skincare
def opcion_skincare():
    print("¿De qué tema quieres saber?\n")
    while True:
        print("Las opciones son:\n-cara\n-cuerpo\n-regresar\n-salir\n")
        opcion=input(">>> ")
        limpiar_pantalla()
        
        validacion=validarOpcion(opcion, matriz_validacion[2])

        if validacion[0]:
            #Opción cara
            if validacion[1]==0:
                opcion_cara()
            #Opción cuerpo
            elif validacion[1]==1:
                opcion_cuerpo()
            #Opción regresar
            elif validacion[1]==2:
                informacion()
            #Si la opción es salir, no se hace nada y se dirige al menú final
            break

#Función del menú de cuidado del cabello
def opcion_cabello():
    #Da información general
    print(cabello[0])
    print("¿Sobre cuál tipo de cabello quieres saber?")
    while True:
        opcion=input("Los tipos son:\n-Rizado\n-Ondulado\n-Lacio\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[7])

        if validacion[0]:
            #Opción Rizado
            if validacion[1]==0:
                #Da información del cabello rizado
                print(cabello[1])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Da la información extra
                            print(cabello[2])
                        break
            #Opción Ondulado
            elif validacion[1]==1:
                #Da información del cabello ondulado
                print(cabello[3])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Da la información extra
                            print(cabello[4])
                        break
            #Opción Lacio
            elif validacion[1]==2:
                #Da información del cabello lacio
                print(cabello[5])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            #Da la información extra
                            print(cabello[6])
                        break
            break

#Función del menú principal
def informacion():
    print("¿De qué tema quieres saber?\n")
    while True:        
        opcion=input("Las opciones son:\n- skincare\n- cuidado del cabello\n\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[1])

        if validacion[0]:
            #Opción skincare
            if validacion[1]==0:
                opcion_skincare()
            #Opción cuidado del cabello
            else:
                opcion_cabello()
            break
    
    #Todos los menús y demás terminan aquí en algún momento, este es el menú final
    print("\n¿Quieres regresar al menú principal?\n")
    while True:
        opcion=input("Debes contestar con si o no\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[0])

        if validacion[0]:
            #Debido a que el menú principal está en informacion(), llamamos esa función y no a main()
            if validacion[1]==0:
                informacion()
            break

def main():
    #Saludamos al usuario y le pedimos su nombre
    print("Hola me llamo Belleza de Gangnam, es un placer conocerte.\n¿Con quién tengo el placer?")
    nombre=(input(">>> "))
    limpiar_pantalla()

    print("Hola",nombre,"es un placer estar contigo, espero que te podamos ayudar en algo")
    inputUsuario()
    limpiar_pantalla()

    print("Calculemos la cantidad recomendada de agua que debes de ingerir al día...")
    while True:
        valid=True
        weight=str(input("Ingresa tu peso en kg: "))
        limpiar_pantalla()
        #Revisa cada carácter del string weight
        for i in weight:
            #Si no está en la lista digitos, esto significa que se ingresó un caracter no valido
            if i not in digitos:
                print("No ingreses letras o simbolos diferentes de '.' en tú respuesta...\n")
                #Invalidamos la opción
                valid=False
        #Si sigue siendo valido, entonces...
        if valid:
            #Se verifica si se ingreso un string vacío o tiene más de un punto...
            if weight=="" or weight.count(".")>1:
                #Se pide que se corriga
                print("Por favor ingresa un número valido...\n")
                valid=False

        if valid:
            #Devuelve la cantidad de mililitros de agua que debe beber la persona (30 por kilo)
            print(f"Para tener una piel saludable, se recomienda consumir aproximadamente {float(weight)*30} ml de agua")
            inputUsuario()
            limpiar_pantalla()
            break

    #Una breve información cómo introducción
    print("Antes de pasar a la información\n"
          "¿Te gustaría una breve definición de skincare y de cuidado del cabello?")
    
    while True:
        opcion=input("Debes contestar con si o no\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[0])

        if validacion[0]:
            if validacion[1]==0:
                #Se da una breve definición de skincare
                print(skincare)
                inputUsuario()
                limpiar_pantalla()
            break

    #Terminada la introducción, se llama al menú principal
    informacion()
    
    #Si en el menú final se pide no regresar, se despide al usuario
    print("Hasta luego,", nombre)

main()
