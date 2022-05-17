#TP8 EJERCICIO 1
'''1. Se necesita crear una agenda electronica, esta agenda empezara en blanco y se podrá 
agregar personas con la siguiente información: Nombre y Apellido, mail, telefono y dirección. 
El programa debe dar un menu de opciones con la posibilidad de:
• Mostrar toda la agenda completa
• Buscar por nombre y apellido (en la búsqueda no tiene que ser necesario que el usuario 
escriba el nombre y apellido completo, por ejemplo si me quiere buscar a mi, con que 
escriba Jav, ya deberían aparecer todas las personas con nombre que empiecen con 
Jav)
• Nueva persona, para agregar una nueva persona a la agenda, en caso de que ya exista 
la persona debería mostrar un error.
• Modificar persona, para modificar algun dato de la persona, al seleccionar esta opcion 
debería aparecer un menu con el dato en especifico que la persona quiere modificar 
(mail, telefono o dirección), en caso de que no exista la persona o el dato a modificar 
debería mostrar un error.
• Eliminar persona, en caso de que no exista debería mostrar un error.'''

#TITULO PROGRAMA
print()
print("Agenda Electronica")

#DATOS

agenda = {}
opcion = 0

while opcion != 6:
    print()
    print("--Menu de opciones--")
    print("1. Mostrar agenda")
    print("2. Buscar contacto")
    print("3. Nuevo contacto")
    print("4. Modificar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    test_opcion = input("Opcion? ")
    print()
    if test_opcion.isdigit() == False:
        print("Ingrese una opcion valida.")
        continue
    else:
        opcion = int(test_opcion)

    if opcion > 6 or opcion < 0:
        print("Opcion invalida")
        input()

    elif opcion == 1:
        print("--Lista de contactos--")
        for x in agenda:
            print(agenda[x])
        
        input()
    
    elif opcion == 2:
        print("--Buscar contacto--")
        busqueda = input("Nombre? ")
        for i in agenda.keys():
            if busqueda in i:
                print(agenda[i])
        input()

    elif opcion == 3:
        print("--Anadir contacto--")
        nombre_apellido = input("Nombre y apellido: ") 
        mail = input("Mail: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")

        if agenda.get(nombre_apellido) == None:
            agenda[nombre_apellido] = {"Nombre y apellido":nombre_apellido, "Mail":mail, "Telefono":telefono, "Direccion":direccion}
            print("Anadido con exito")
            input()
        else:
            print("El nombre ya existe. Para modificar un contacto ingrese la opcion 4")
            input()
    
    elif opcion == 4:
        print("--Modificar contacto--")
        nombre_apellido = input('Que contacto desea modificar?: ')
        if agenda.get(nombre_apellido) == None:
            print('El contacto no existe.')
        else:
            while True:
                print ('-----------------')
                print ('1. Mail')
                print ('2. Telefono')
                print ('3. Dirección')
                print ('4. Finalizar')
                print ('-----------------')
                test_opcion2 = input('Que opcion desea modificar?: ')

                if test_opcion2.isdigit() == False:
                    print("Ingrese una opcion valida.")
                    continue
                else:
                    opcion2 = int(test_opcion2)

                if opcion2 == 1:
                    mail = input('Ingrese el nuevo mail: ')
                    agenda[nombre_apellido]['Mail'] = mail 
                elif opcion2 == 2:
                    telefono = (input('Ingrese el nuevo telefono: '))
                    agenda[nombre_apellido]['Telefono'] = telefono
                elif opcion2 == 3:
                    direccion = input('Ingrese la nueva dirección: ')
                    agenda[nombre_apellido]['Dirección'] = direccion
                elif opcion2 == 4:
                    break
                else:
                    print('Opcion incorrecta')

    elif opcion == 5:
        print("--Eliminar contacto--")
        nombre_apellido = input('Ingrese contacto a eliminar: ')
        if agenda.get(nombre_apellido) == None:
            print('El contacto no existe')
            input()
        else:
            agenda.pop(nombre_apellido)
            print("Contacto eliminado")
            input()


            
     


        