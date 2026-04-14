# Proyecto Mapa de Puntos de Interés

## Descripción
Este proyecto es una aplicación web que permite registrar y visualizar puntos de interés en un mapa interactivo.  
Los puntos pueden filtrarse por categoría y por radio de búsqueda usando coordenadas geográficas.

## Tecnologías utilizadas
- Backend: Python (Flask)
- Base de datos: PostgreSQL + PostGIS
- Frontend: HTML, JavaScript, Leaflet
- Contenedores: Docker y Docker Compose
- Servidor web: Nginx

## Funcionalidades
- Registro de puntos con:
  - Nombre
  - Descripción
  - Categoría
  - Coordenadas (latitud y longitud)
- Visualización de puntos en mapa interactivo
- Selección de ubicación haciendo clic en el mapa
- Filtrado por:
  - Categoría
  - Radio en metros desde un punto
- Persistencia de datos usando PostgreSQL

## Estructura del proyecto
- app.py → Backend Flask
- init.sql → Inicialización de base de datos
- Dockerfile → Configuración del backend
- docker-compose.yml → Orquestación de servicios
- index.html → Interfaz web

## Cómo ejecutar el proyecto

### Requisitos
- Docker instalado
- Docker Compose instalado

### Pasos
1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/proyecto-mapa.git

2. Entrar al proyecto:
   cd proyecto-mapa

3. Levantar los contenedores:
   docker-compose up --build

4. Abrir en navegador:
   http://localhost

## Uso
1. Hacer clic en el mapa para seleccionar coordenadas
2. Completar los datos del punto
3. Guardar el punto
4. Usar filtros por radio y categoría
5. Visualizar resultados en el mapa

## Notas
- Los datos se almacenan en un volumen de Docker
- Para reiniciar completamente la base de datos:
  docker-compose down -v

## Autor
Madelin Velvet Mendoza Bedoya
