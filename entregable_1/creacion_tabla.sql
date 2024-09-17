CREATE TABLE turnosfarmaciasChile (
    fecha DATE,
    local_id INT,
    fk_region INT,
    fk_comuna INT,
    fk_localidad INT,
    local_nombre NVARCHAR(50),
    comuna_nombre NVARCHAR(50),
    localidad_nombre NVARCHAR(50),
    local_direccion NVARCHAR(100),
    funcionamiento_hora_apertura TIME,
    funcionamiento_hora_cierre TIME,
    local_telefono NVARCHAR(50),
    local_lat NVARCHAR(50),
    local_lng NVARCHAR(50),
    funcionamiento_dia NVARCHAR(50)
);