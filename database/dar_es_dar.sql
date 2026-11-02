-- Base de datos Dar es Dar
-- Ejecutar en MySQL Workbench.
CREATE DATABASE IF NOT EXISTS dar_es_dar;
USE dar_es_dar;

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

CREATE TABLE Socio (
    idSocio INT AUTO_INCREMENT PRIMARY KEY,
    numeroSocio INT NOT NULL UNIQUE,
    sector VARCHAR(80),
    gerencia VARCHAR(80),
    idPersona INT NOT NULL UNIQUE,
    FOREIGN KEY (idPersona) REFERENCES Persona(idPersona)
);

CREATE TABLE Familiar (
    idFamiliar INT AUTO_INCREMENT PRIMARY KEY,
    idSocio INT NOT NULL,
    idPersona INT NOT NULL UNIQUE,
    parentesco VARCHAR(40),
    FOREIGN KEY (idSocio) REFERENCES Socio(idSocio),
    FOREIGN KEY (idPersona) REFERENCES Persona(idPersona)
);

CREATE TABLE Beneficio (
    idBeneficio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE Solicitud (
    idSolicitud INT AUTO_INCREMENT PRIMARY KEY,
    idSocio INT NOT NULL,
    idBeneficio INT NOT NULL,
    fecha DATE,
    estado VARCHAR(30) NOT NULL DEFAULT 'Pendiente',
    FOREIGN KEY (idSocio) REFERENCES Socio(idSocio),
    FOREIGN KEY (idBeneficio) REFERENCES Beneficio(idBeneficio)
);

INSERT INTO Beneficio (nombre, descripcion) VALUES
('Electronica', 'Productos de electronica'),
('Almacen', 'Productos de almacen'),
('Adelanto de sueldo', 'Adelanto de sueldo para socios'),
('Prestamo', 'Prestamos para socios'),
('Sepelio', 'Servicio de sepelio'),
('Asesoria juridica', 'Asesoramiento juridico'),
('Asesoria de seguros', 'Asesoramiento sobre seguros'),
('Utiles escolares', 'Entrega de utiles escolares'),
('Optica', 'Beneficio de optica');
