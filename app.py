from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",
        database="mapas",
        user="user",
        password="password"
    )

@app.route('/')
def home():
    return "API funcionando con base de datos"

# 🔹 Obtener todos los puntos
@app.route('/api/puntos')
def obtener_puntos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nombre, descripcion, categoria,
               ST_Y(ubicacion::geometry),
               ST_X(ubicacion::geometry)
        FROM puntos;
    """)

    puntos = []
    for row in cursor.fetchall():
        puntos.append({
            "nombre": row[0],
            "descripcion": row[1],
            "categoria": row[2],
            "lat": float(row[3]),
            "lng": float(row[4])
        })

    cursor.close()
    conn.close()

    return jsonify(puntos)


@app.route('/api/puntos/filtro')
def filtrar_puntos():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radio = request.args.get('radio')
    categoria = request.args.get('categoria')

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT nombre, descripcion, categoria,
               ST_Y(ubicacion::geometry),
               ST_X(ubicacion::geometry)
        FROM puntos
    """

    condiciones = []
    params = []

    # filtro por categoria
    if categoria and categoria != "":
        condiciones.append("categoria = %s")
        params.append(categoria)

    # filtro por radio
    if lat and lng and radio and radio != "":
        condiciones.append("""
            ST_DWithin(
                ubicacion,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
                %s
            )
        """)
        params.extend([float(lng), float(lat), float(radio)])

    # aplicar condiciones
    if condiciones:
        query += " WHERE " + " AND ".join(condiciones)

    cursor.execute(query, params)

    puntos = []
    for row in cursor.fetchall():
        puntos.append({
            "nombre": row[0],
            "descripcion": row[1],
            "categoria": row[2],
            "lat": float(row[3]),
            "lng": float(row[4])
        })

    cursor.close()
    conn.close()

    return jsonify(puntos)  

@app.route('/api/puntos', methods=['POST'])
def agregar_punto():
    data = request.json

    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    categoria = data.get('categoria')
    lat = data.get('lat')
    lng = data.get('lng')

    if not all([nombre, descripcion, categoria, lat, lng]):
        return jsonify({"error": "Datos incompletos"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO puntos (nombre, descripcion, categoria, ubicacion)
        VALUES (%s, %s, %s,
            ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography
        )
    """, (nombre, descripcion, categoria, lng, lat))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Punto agregado correctamente"})

    if categoria and categoria != "":
        if categoria == "salud":
            condiciones.append("categoria IN ('salud', 'farmacia', 'hospital')")
        elif categoria == "cultural":
            condiciones.append("categoria IN ('cultural', 'iglesia', 'monumento')")
        elif categoria == "gastronomico":
            condiciones.append("categoria IN ('gastronomico', 'comida_rapida', 'restaurante')")
        else:
            condiciones.append("categoria = %s")
            params.append(categoria)

    if lat and lng and radio and radio != "":
        condiciones.append("""
            ST_DWithin(
                ubicacion,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
                %s
            )
        """)
        params.extend([float(lng), float(lat), float(radio)])

    if condiciones:
        query += " WHERE " + " AND ".join(condiciones)

    cursor.execute(query, params)

    puntos = []
    for row in cursor.fetchall():
        puntos.append({
            "nombre": row[0],
            "descripcion": row[1],
            "categoria": row[2],
            "lat": float(row[3]),
            "lng": float(row[4])
        })

    cursor.close()
    conn.close()

    return jsonify(puntos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)