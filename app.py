from flask import Flask, Response, jsonify, request
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)
app.secret_key="rubendc2001dic12dia1adad"

#Configurar conexion a base de datos
app.config["MYSQL_HOST"] = "Rubendc1412.mysql.pythonanywhere-services.com"
app.config["MYSQL_USER"] = "Rubendc1412"
app.config["MYSQL_PASSWORD"] = "M0rg4ngh0$T$"
app.config["MYSQL_DB"] = "Rubendc1412$meta"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

#Establecer la configuracion anterior
mysql = MySQL(app)

@app.route('/datos')
def obtener_datos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM AppData')
    datos = []
    for row in cursor.fetchall():
        dato = {
            'Municipio': row[0],
            'Estado': row[1],
            'Etnia': row[2],
            'Secciones': row[3],
            'Porcentaje': row[4],
            'Meta': row[5],
            'Habitantes': row[6],
            'Localidades': row[7],
        }
        datos.append(dato)
    return jsonify({'datos': datos}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT AppUserId, AppUserName, AppUserPassword FROM AppUsers WHERE AppUserName = ? AND AppUserPassword = ?", (username, password))
    user = cursor.fetchone()
    if user:
        user_data = {
            'id': user[0],
            'username': user[1],
            'password': user[2]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'error': 'Datos incorrectos'}), 401

@app.route('/logout', methods=['POST'])
def logout():
        return jsonify({'mensaje': 'Se ha cerrado la sesion'}), 200

if __name__ == '__main__':
    app.run(debug=True)