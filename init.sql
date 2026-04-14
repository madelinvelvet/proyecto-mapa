CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS puntos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    categoria TEXT,
    ubicacion GEOGRAPHY(Point, 4326)
);

INSERT INTO puntos (nombre, descripcion, categoria, ubicacion) VALUES
('Parque Central', 'Lugar turistico', 'cultural', ST_MakePoint(-90.5069, 14.6349)),
('Gasolinera Shell', 'Estacion de servicio', 'servicio', ST_MakePoint(-90.5075, 14.6355)),
('Restaurante La Casa', 'Comida tipica', 'gastronomico', ST_MakePoint(-90.5080, 14.6360)),
('Hospital General', 'Centro medico', 'salud', ST_MakePoint(-90.5090, 14.6370)),
('Monumento Historico', 'Sitio cultural', 'cultural', ST_MakePoint(-90.5100, 14.6380)),
('Cafe Central', 'Cafeteria', 'cafeteria', ST_MakePoint(-90.5110, 14.6390)),
('Parque Ecologico', 'area natural', 'natural', ST_MakePoint(-90.5120, 14.6400)),
('Banco Nacional', 'Servicios financieros', 'financiero', ST_MakePoint(-90.5130, 14.6410));

-- FARMACIAS
INSERT INTO puntos (nombre, descripcion, categoria, ubicacion) VALUES
('Farmacia Cruz Verde', 'Medicamentos', 'farmacia', ST_MakePoint(-90.5140, 14.6420)),
('Farmacia Galeno', 'Atencion medica', 'farmacia', ST_MakePoint(-90.5150, 14.6430));

-- IGLESIAS
INSERT INTO puntos (nombre, descripcion, categoria, ubicacion) VALUES
('Iglesia Central', 'Templo religioso', 'iglesia', ST_MakePoint(-90.5160, 14.6440));

-- COMIDA RAPIDA
INSERT INTO puntos (nombre, descripcion, categoria, ubicacion) VALUES
('Burger Express', 'Comida rapida', 'comida_rapida', ST_MakePoint(-90.5170, 14.6450));