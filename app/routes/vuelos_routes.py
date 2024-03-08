# app/routes/vuelos_routes.py
from flask import Blueprint, jsonify, request
from database import get_db_connection

vuelos_bp = Blueprint('vuelos_bp', __name__)

@vuelos_bp.route('/', methods=['GET', 'POST'])
def vuelos():
    if request.method == 'GET':
        # Operación de lectura para obtener la lista de vuelos
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM vuelos')
                result = cursor.fetchall()
                return jsonify(result)
        finally:
            connection.close()

    elif request.method == 'POST':
        # Operación de creación para agregar un nuevo vuelo
        nuevo_vuelo = request.json
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO vuelos (origen, destino, fecha_salida, precio, plazas_disponibles) '
                               'VALUES (%s, %s, %s, %s, %s)',
                               (nuevo_vuelo['origen'], nuevo_vuelo['destino'], nuevo_vuelo['fecha_salida'],
                                nuevo_vuelo['precio'], nuevo_vuelo['plazas_disponibles']))
                connection.commit()
                return jsonify({'message': 'Vuelo creado exitosamente'})
        finally:
            connection.close()

@vuelos_bp.route('/<int:vuelo_id>', methods=['GET', 'PUT', 'DELETE'])
def vuelo_detalle(vuelo_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            if request.method == 'GET':
                # Operación de lectura para obtener detalles de un vuelo específico
                cursor.execute('SELECT * FROM vuelos WHERE id = %s', (vuelo_id,))
                result = cursor.fetchone()
                return jsonify(result) if result else jsonify({'message': 'Vuelo no encontrado'}), 404

            elif request.method == 'PUT':
                # Operación de actualización para modificar un vuelo específico
                datos_actualizados = request.json
                cursor.execute('UPDATE vuelos SET origen=%s, destino=%s, fecha_salida=%s, precio=%s, '
                               'plazas_disponibles=%s WHERE id=%s',
                               (datos_actualizados['origen'], datos_actualizados['destino'],
                                datos_actualizados['fecha_salida'], datos_actualizados['precio'],
                                datos_actualizados['plazas_disponibles'], vuelo_id))
                connection.commit()
                return jsonify({'message': 'Vuelo actualizado exitosamente'})

            elif request.method == 'DELETE':
                # Operación de eliminación para borrar un vuelo específico
                cursor.execute('DELETE FROM vuelos WHERE id=%s', (vuelo_id,))
                connection.commit()
                return jsonify({'message': 'Vuelo eliminado exitosamente'})
    finally:
        connection.close()
