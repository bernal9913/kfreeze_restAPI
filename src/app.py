from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)
cnx = MySQL(app)

@app.route('/users')
def list_users():
    try:
        cur = cnx.connection.cursor()
        sql = "SELECT * FROM users "
        cur.execute(sql)
        dato = cur.fetchall()
        print(dato)
        return "table founded!"
    except Exception as ex:
        cur = cnx.connection.cursor()
        sql = "SELECT * FROM 'users1' "
        cur.execute(sql)
        dato = cur.fetchall()
        print(dato)
        return "Error"

def page_not_found(error):
    return "<h1>Yo habia ponido una Steph aqui y no esta</h1>", 404

if __name__ == '__main__':
    # conda activate RestApi
    # db.execSQL("CREATE TABLE users(username text PRIMARY KEY, email text, password text, birthdate text, nacion text)");
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
    