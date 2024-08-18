class Paciente:
    def __init__(self, nombre, cedula, genero, servicio):
        self.nombre = nombre
        self.cedula = cedula
        self.genero = genero
        self.servicio = servicio

    def __str__(self):
        return (f'Paciente con los siguientes datos: Nombre: {self.nombre}, Cédula: {self.cedula}, Género: {self.genero}, Servicio: {self.servicio}')

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []

    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = input("Ingrese la cédula: ")
        genero = input("Ingrese el género: ")
        servicio = input("Ingrese el servicio: ")
        p = Paciente(nombre, cedula, genero, servicio)
        self.__lista_pacientes.append(p)

    def verDatos(self, cedula):
        for paciente in self.__lista_pacientes:
            if paciente.cedula == cedula:
                print(paciente)
                return
        print('Paciente no encontrado.')

    def numPacientes(self):
        print(f'El número de pacientes en el sistema: {len(self.__lista_pacientes)}')

miSistema = Sistema()

while True:
    opcion = int(input('1. Ingresar un nuevo paciente\n2. Ver el número de pacientes\n3. Ver los datos de un paciente\n4. Salir\n '))
    
    if opcion == 1:
        miSistema.ingresarPaciente()
        
    elif opcion == 2:
        miSistema.numPacientes()
        
    elif opcion == 3:
        cedula = input('Ingrese la cédula del paciente: ')
        miSistema.verDatos(cedula)
        
    elif opcion == 4:
        print('Gracias por usar, saliendo del sistema... ')
        break
        
    else: 
        print('Ingrese una opción correcta.')

    