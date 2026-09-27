#Persona
class Persona:

    def __init__(self, nombre, apellido, fechaNacimiento, documento,
                 cuil, nacionalidad, estadoCivil, genero, correo,
                 direccion, codigoPostal, ciudad, telefono):

        self.Nombre = nombre
        self.Apellido = apellido
        self.FechaNacimiento = fechaNacimiento
        self.Documento = documento
        self.Cuil = cuil
        self.Nacionalidad = nacionalidad
        self.EstadoCivil = estadoCivil
        self.Genero = genero
        self.Correo = correo
        self.Direccion = direccion
        self.CodigoPostal = codigoPostal
        self.Ciudad = ciudad
        self.Telefono = telefono

    def verDatos(self):

        print("Nombre y apellido:", self.Nombre, self.Apellido)
        print("Fecha de nacimiento:", self.FechaNacimiento)
        print("DNI / LE / LC:", self.Documento)
        print("CUIL:", self.Cuil)
        print("Nacionalidad:", self.Nacionalidad)
        print("Estado civil:", self.EstadoCivil)
        print("Genero:", self.Genero)
        print("Correo:", self.Correo)
        print("Direccion:", self.Direccion)
        print("Codigo Postal:", self.CodigoPostal)
        print("Ciudad:", self.Ciudad)
        print("Telefono:", self.Telefono)

#Socio
class Socio(Persona):

    def __init__(self, nombre, apellido, fechaNacimiento, documento,
                 cuil, nacionalidad, estadoCivil, genero, correo,
                 direccion, codigoPostal, ciudad, telefono,
                 numeroSocio, sector, gerencia):

        super().__init__(
            nombre,
            apellido,
            fechaNacimiento,
            documento,
            cuil,
            nacionalidad,
            estadoCivil,
            genero,
            correo,
            direccion,
            codigoPostal,
            ciudad,
            telefono
        )

        self.NumeroSocio = numeroSocio
        self.Sector = sector
        self.Gerencia = gerencia

        self.Familiares = []
        self.Solicitudes = []

    def verDatos(self):

        print("\nDATOS DEL SOCIO")

        print("Numero de socio:", self.NumeroSocio)
        print("Sector:", self.Sector)
        print("Gerencia:", self.Gerencia)

        super().verDatos()

#Familiar
class Familiar(Persona):

    def __init__(self, nombre, apellido, fechaNacimiento, documento,
                 genero, parentesco):

        super().__init__(
            nombre,
            apellido,
            fechaNacimiento,
            documento,
            "",
            "",
            "",
            genero,
            "",
            "",
            "",
            "",
            ""
        )

        self.Parentesco = parentesco

    def verDatos(self):

        print("Nombre y apellido:", self.Nombre, self.Apellido)
        print("Genero:", self.Genero)
        print("Fecha de nacimiento:", self.FechaNacimiento)
        print("DNI / LE / LC:", self.Documento)
        print("Parentesco:", self.Parentesco)

#Beneficio
class Beneficio:

    def __init__(self, codigo, nombre, descripcion):

        self.Codigo = codigo
        self.Nombre = nombre
        self.Descripcion = descripcion

    def verDatos(self):

        print("Codigo:", self.Codigo)
        print("Beneficio:", self.Nombre)
        print("Descripcion:", self.Descripcion)

#Proveeduria
class Proveeduria(Beneficio):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

        self.Rubro = rubro

#Electronica
class Electronica(Proveeduria):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion,
            rubro
        )

#Almacen
class Almacen(Proveeduria):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion,
            rubro
        )

#AdelantoSueldo
class AdelantoSueldo(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Prestamo
class Prestamo(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Sepelio
class Sepelio(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Asesoria
class Asesoria(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Asesoria Juridica
class AsesoriaJuridica(Asesoria):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Clase Asesoria Seguros
class AsesoriaSeguros(Asesoria):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Utiles Escolares
class UtilesEscolares(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Optica
class Optica(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

#Solicitud
class Solicitud:

    def __init__(self, numero, beneficio):

        self.Numero = numero
        self.Beneficio = beneficio
        self.Estado = "Pendiente"

    def verDatos(self):

        print("Numero de solicitud:", self.Numero)
        print("Beneficio:", self.Beneficio.Nombre)
        print("Estado:", self.Estado)

#Listas del sistema
socios = []
beneficios = []
solicitudes = []

#Beneficios
beneficios.append(
    Electronica(
        1,
        "Electronica",
        "Productos de electronica",
        "Proveeduria"
    )
)

beneficios.append(
    Almacen(
        2,
        "Almacen",
        "Productos de almacen",
        "Proveeduria"
    )
)

beneficios.append(
    AdelantoSueldo(
        3,
        "Adelanto de sueldo",
        "Adelanto de sueldo para socios"
    )
)

beneficios.append(
    Prestamo(
        4,
        "Prestamo",
        "Prestamos para socios"
    )
)

beneficios.append(
    Sepelio(
        5,
        "Sepelio",
        "Servicio de sepelio"
    )
)

beneficios.append(
    AsesoriaJuridica(
        6,
        "Asesoria juridica",
        "Asesoramiento juridico"
    )
)

beneficios.append(
    AsesoriaSeguros(
        7,
        "Asesoria de seguros",
        "Asesoramiento sobre seguros"
    )
)

beneficios.append(
    UtilesEscolares(
        8,
        "Utiles escolares",
        "Entrega de utiles escolares"
    )
)

beneficios.append(
    Optica(
        9,
        "Optica",
        "Beneficio de optica"
    )
)


# Buscar socio

def buscarSocio(numero):

    for socio in socios:

        if socio.NumeroSocio == numero:

            return socio

    return None

#Alta de socio
def altaSocio():

    print("\nALTA DE SOCIO")

    print("\nDATOS PERSONALES")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fechaNacimiento = input("Fecha de nacimiento: ")
    documento = input("DNI / LE / LC: ")
    cuil = input("CUIL: ")
    nacionalidad = input("Nacionalidad: ")
    estadoCivil = input("Estado civil: ")
    genero = input("Genero: ")
    correo = input("Correo: ")
    direccion = input("Direccion: ")
    codigoPostal = input("Codigo Postal: ")
    ciudad = input("Ciudad: ")
    telefono = input("Telefono: ")

    print("\nDATOS LABORALES")

    numeroSocio = input("Numero de socio: ")
    sector = input("Sector: ")
    gerencia = input("Gerencia: ")

    socio = Socio(
        nombre,
        apellido,
        fechaNacimiento,
        documento,
        cuil,
        nacionalidad,
        estadoCivil,
        genero,
        correo,
        direccion,
        codigoPostal,
        ciudad,
        telefono,
        numeroSocio,
        sector,
        gerencia
    )

    socios.append(socio)

    print("\nSocio registrado correctamente.")

    input("\nPresione ENTER para volver al menu...")

#Consultar socio
def consultarSocio():

    print("\nCONSULTAR SOCIO")

    numero = input("Ingrese el numero de socio: ")

    socio = buscarSocio(numero)

    if socio == None:

        print("\nNo se encontro el socio.")

    else:

        socio.verDatos()

        print("\nGRUPO FAMILIAR")

        if len(socio.Familiares) == 0:

            print("No tiene familiares registrados.")

        else:

            for familiar in socio.Familiares:

                print("\n")
                familiar.verDatos()


        print("\nSOLICITUDES")

        if len(socio.Solicitudes) == 0:

            print("No tiene solicitudes.")

        else:

            for solicitud in socio.Solicitudes:

                print("\n")
                solicitud.verDatos()

    input("\nPresione ENTER para volver al menu...")

#Listar socios
def listarSocios():

    print("\nLISTADO DE SOCIOS")

    if len(socios) == 0:

        print("No hay socios registrados.")

    else:

        for socio in socios:

            print(
                "Numero:",
                socio.NumeroSocio,
                "-",
                socio.Nombre,
                socio.Apellido
            )

    input("\nPresione ENTER para volver al menu...")

#Modificar socio
def modificarSocio():

    print("\nMODIFICAR SOCIO")

    numero = input("Ingrese el numero de socio: ")

    socio = buscarSocio(numero)

    if socio == None:

        print("\nNo se encontro el socio.")

    else:

        print("\nDatos actuales:")

        socio.verDatos()

        print("\nIngrese los nuevos datos:")

        socio.Nombre = input("Nuevo nombre: ")
        socio.Apellido = input("Nuevo apellido: ")
        socio.FechaNacimiento = input("Nueva fecha de nacimiento: ")
        socio.Documento = input("Nuevo DNI / LE / LC: ")
        socio.Cuil = input("Nuevo CUIL: ")
        socio.Nacionalidad = input("Nueva nacionalidad: ")
        socio.EstadoCivil = input("Nuevo estado civil: ")
        socio.Genero = input("Nuevo genero: ")
        socio.Correo = input("Nuevo correo: ")
        socio.Direccion = input("Nueva direccion: ")
        socio.CodigoPostal = input("Nuevo Codigo Postal: ")
        socio.Ciudad = input("Nueva ciudad: ")
        socio.Telefono = input("Nuevo telefono: ")
        socio.Sector = input("Nuevo sector: ")
        socio.Gerencia = input("Nueva gerencia: ")

        print("\nDatos modificados correctamente.")

    input("\nPresione ENTER para volver al menu...")

#Eliminar socio
def eliminarSocio():

    print("\nELIMINAR SOCIO")

    numero = input("Ingrese el numero de socio: ")

    socio = buscarSocio(numero)

    if socio == None:

        print("\nNo se encontro el socio.")

    else:

        socio.verDatos()

        respuesta = input(
            "\n¿Desea eliminar este socio? (S/N): "
        )

        if respuesta == "S" or respuesta == "s":

            socios.remove(socio)

            print("\nSocio eliminado correctamente.")

        else:

            print("\nOperacion cancelada.")

    input("\nPresione ENTER para volver al menu...")

#Agregar familiar
def agregarFamiliar():

    print("\nAGREGAR FAMILIAR")

    numero = input("Ingrese el numero de socio: ")

    socio = buscarSocio(numero)

    if socio == None:

        print("\nNo se encontro el socio.")

    else:

        print("\nDATOS DEL FAMILIAR")

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        genero = input("Genero: ")
        fechaNacimiento = input("Fecha de nacimiento: ")
        documento = input("DNI / LE / LC: ")
        parentesco = input("Parentesco: ")

        familiar = Familiar(
            nombre,
            apellido,
            fechaNacimiento,
            documento,
            genero,
            parentesco
        )

        socio.Familiares.append(familiar)

        print("\nFamiliar agregado correctamente.")

    input("\nPresione ENTER para volver al menu...")

# Ver beneficios
def verBeneficios():

    print("\nBENEFICIOS DISPONIBLES")

    for beneficio in beneficios:

        print(
            beneficio.Codigo,
            "-",
            beneficio.Nombre
        )

    input("\nPresione ENTER para volver al menu...")

#Solicitar beneficio
def solicitarBeneficio():

    print("\nSOLICITAR BENEFICIO")

    numero = input("Ingrese el numero de socio: ")

    socio = buscarSocio(numero)

    if socio == None:

        print("\nNo se encontro el socio.")

    else:

        print("\nBENEFICIOS DISPONIBLES")

        for beneficio in beneficios:

            print(
                beneficio.Codigo,
                "-",
                beneficio.Nombre
            )

        codigo = int(
            input("\nIngrese el codigo del beneficio: ")
        )

        beneficioElegido = None

        for beneficio in beneficios:

            if beneficio.Codigo == codigo:

                beneficioElegido = beneficio


        if beneficioElegido == None:

            print("\nNo existe ese beneficio.")

        else:

            numeroSolicitud = len(solicitudes) + 1

            solicitud = Solicitud(
                numeroSolicitud,
                beneficioElegido
            )

            socio.Solicitudes.append(solicitud)

            solicitudes.append(solicitud)

            print("\nSolicitud registrada correctamente.")

            print(
                "Numero de solicitud:",
                numeroSolicitud
            )

    input("\nPresione ENTER para volver al menu...")

#Actualizar solicitud
def actualizarSolicitud():

    print("\nACTUALIZAR SOLICITUD")

    numero = int(
        input("Ingrese el numero de solicitud: ")
    )

    solicitudEncontrada = None

    for solicitud in solicitudes:

        if solicitud.Numero == numero:

            solicitudEncontrada = solicitud


    if solicitudEncontrada == None:

        print("\nNo se encontro la solicitud.")

    else:

        print("\nSolicitud encontrada:")

        solicitudEncontrada.verDatos()

        print("\n1 - Pendiente")
        print("2 - Aprobada")
        print("3 - Rechazada")

        opcion = input(
            "\nSeleccione el nuevo estado: "
        )

        if opcion == "1":

            solicitudEncontrada.Estado = "Pendiente"

        elif opcion == "2":

            solicitudEncontrada.Estado = "Aprobada"

        elif opcion == "3":

            solicitudEncontrada.Estado = "Rechazada"

        else:

            print("\nOpcion incorrecta.")

        print("\nSolicitud actualizada.")

    input("\nPresione ENTER para volver al menu...")

#Menu

def menu():

    opcion = ""

    while opcion != "0":

        print("\n")
        print("==============================================")
        print("     SISTEMA DE GESTION DE SOCIOS")
        print("                DAR ES DAR")
        print("==============================================")

        print("1 - Alta de socio")
        print("2 - Consultar socio")
        print("3 - Listar socios")
        print("4 - Modificar socio")
        print("5 - Eliminar socio")
        print("6 - Agregar familiar")
        print("7 - Ver beneficios")
        print("8 - Solicitar beneficio")
        print("9 - Actualizar solicitud")
        print("0 - Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            altaSocio()

        elif opcion == "2":

            consultarSocio()

        elif opcion == "3":

            listarSocios()

        elif opcion == "4":

            modificarSocio()

        elif opcion == "5":

            eliminarSocio()

        elif opcion == "6":

            agregarFamiliar()

        elif opcion == "7":

            verBeneficios()

        elif opcion == "8":

            solicitarBeneficio()

        elif opcion == "9":

            actualizarSolicitud()

        elif opcion == "0":

            print("\nFin del sistema.")
            print("Gracias por utilizar Dar es Dar.")

        else:

            print("\nOpcion incorrecta.")

            input(
                "\nPresione ENTER para volver al menu..."
            )

#Inicio
menu()
