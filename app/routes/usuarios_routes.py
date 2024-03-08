# app/routes/usuarios_routes.py
from flask import Blueprint, jsonify, request
from database import get_db_connection

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route('/', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        # Operación de lectura para obtener la lista de usuarios
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM usuarios')
                result = cursor.fetchall()
                return jsonify(result)
        finally:
            connection.close()

    elif request.method == 'POST':
        # Operación de creación para agregar un nuevo usuario
        nuevo_usuario = request.json
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)',
                               (nuevo_usuario['nombre'], nuevo_usuario['email'], nuevo_usuario['contrasena']))
                connection.commit()
                return jsonify({'message': 'Usuario creado exitosamente'})
        finally:
            connection.close()

@usuarios_bp.route('/<int:usuario_id>', methods=['GET', 'PUT', 'DELETE'])
def usuario_detalle(usuario_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            if request.method == 'GET':
                # Operación de lectura para obtener detalles de un usuario específico
                cursor.execute('SELECT * FROM usuarios WHERE id = %s', (usuario_id,))
                result = cursor.fetchone()
                return jsonify(result) if result else jsonify({'message': 'Usuario no encontrado'}), 404

            elif request.method == 'PUT':
                # Operación de actualización para modificar un usuario específico
                datos_actualizados = request.json
                cursor.execute('UPDATE usuarios SET nombre=%s, email=%s, contrasena=%s WHERE id=%s',
                               (datos_actualizados['nombre'], datos_actualizados['email'],
                                datos_actualizados['contrasena'], usuario_id))
                connection.commit()
                return jsonify({'message': 'Usuario actualizado exitosamente'})

            elif request.method == 'DELETE':
                # Operación de eliminación para borrar un usuario específico
                cursor.execute('DELETE FROM usuarios WHERE id=%s', (usuario_id,))
                connection.commit()
                return jsonify({'message': 'Usuario eliminado exitosamente'})
    finally:
        connection.close()
