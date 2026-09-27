-- Base de datos: Dar es Dar
--Tabla Persona
CREATE TABLE Persona (
    idPersona INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fechaNacimiento DATE,
    documento VARCHAR(20),
    cuil VARCHAR(20),
    nacionalidad VARCHAR(40),
    estadoCivil VARCHAR(30),
    genero VARCHAR(30),
    correo VARCHAR(100),
    direccion VARCHAR(100),
    codigoPostal VARCHAR(15),
    ciudad VARCHAR(50),
    telefono VARCHAR(30)
);

--Tabla Socio
CREATE TABLE Socio (
    idSocio INT AUTO_INCREMENT PRIMARY KEY,
    numeroSocio INT NOT NULL UNIQUE,
    sector VARCHAR(80),
    gerencia VARCHAR(80),
    idPersona INT NOT NULL UNIQUE,
    FOREIGN KEY (idPersona)
        REFERENCES Persona(idPersona)
);

--Tabla Familiar
CREATE TABLE Familiar (
    idFamiliar INT AUTO_INCREMENT PRIMARY KEY,
    idSocio INT NOT NULL,
    idPersona INT NOT NULL UNIQUE,
    parentesco VARCHAR(40),
    FOREIGN KEY (idSocio)
        REFERENCES Socio(idSocio),
    FOREIGN KEY (idPersona)
        REFERENCES Persona(idPersona)
);

--Tabla Beneficio
CREATE TABLE Beneficio (
    idBeneficio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    descripcion VARCHAR(255)
);

--Tabla Solicitud
CREATE TABLE Solicitud (
    idSolicitud INT AUTO_INCREMENT PRIMARY KEY,
    idSocio INT NOT NULL,
    idBeneficio INT NOT NULL,
    fecha DATE,
    estado VARCHAR(30) NOT NULL DEFAULT 'Pendiente',
    FOREIGN KEY (idSocio)
        REFERENCES Socio(idSocio),
    FOREIGN KEY (idBeneficio)
        REFERENCES Beneficio(idBeneficio)
);

--Carga de beneficios
INSERT INTO Beneficio (nombre, descripcion)
VALUES
('Electrónica', 'Solicitud electronica'),
('Almacén', 'Solicitud proveeduria'),
('Adelanto de sueldo', 'Solicitud de adelanto de sueldo'),
('Préstamo', 'Solicitud de préstamo'),
('Sepelio', 'Beneficio de sepelio'),
('Asesoría jurídica', 'Asesoramiento jurídico'),
('Asesoría de seguros', 'Asesoramiento sobre seguros'),
('Útiles escolares', 'Entrega de útiles escolares'),
('Óptica', 'Solicitud óptica');
