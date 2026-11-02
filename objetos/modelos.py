# Clase Persona

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


# Clase Socio

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


# Clase Familiar

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


# Clase Beneficio

class Beneficio:

    def __init__(self, codigo, nombre, descripcion):

        self.Codigo = codigo
        self.Nombre = nombre
        self.Descripcion = descripcion

    def verDatos(self):

        print("Codigo:", self.Codigo)
        print("Beneficio:", self.Nombre)
        print("Descripcion:", self.Descripcion)


# Clase Proveeduria

class Proveeduria(Beneficio):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )

        self.Rubro = rubro


# Clase Electronica

class Electronica(Proveeduria):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion,
            rubro
        )


# Clase Almacen

class Almacen(Proveeduria):

    def __init__(self, codigo, nombre, descripcion, rubro):

        super().__init__(
            codigo,
            nombre,
            descripcion,
            rubro
        )


# Clase AdelantoSueldo

class AdelantoSueldo(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase Prestamo

class Prestamo(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase Sepelio

class Sepelio(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase Asesoria

class Asesoria(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase AsesoriaJuridica

class AsesoriaJuridica(Asesoria):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase AsesoriaSeguros

class AsesoriaSeguros(Asesoria):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase UtilesEscolares

class UtilesEscolares(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase Optica

class Optica(Beneficio):

    def __init__(self, codigo, nombre, descripcion):

        super().__init__(
            codigo,
            nombre,
            descripcion
        )


# Clase Solicitud

class Solicitud:

    def __init__(self, numero, beneficio):

        self.Numero = numero
        self.Beneficio = beneficio
        self.Estado = "Pendiente"

    def verDatos(self):

        print("Numero de solicitud:", self.Numero)
        print("Beneficio:", self.Beneficio.Nombre)
        print("Estado:", self.Estado)
