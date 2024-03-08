CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);
CREATE TABLE vuelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(255) NOT NULL,
    destino VARCHAR(255) NOT NULL,
    fecha_salida DATE NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    plazas_disponibles INT NOT NULL
);
