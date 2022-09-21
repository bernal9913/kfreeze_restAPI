from crypt import methods

from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)
cnx = MySQL(app)
@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/users', methods=['GET'])
def list_users():
    try:
        cur = cnx.connection.cursor()
        sql = "SELECT * FROM users "
        cur.execute(sql)
        dato = cur.fetchall()
        usrs = []
        for f in dato:
            usr = {'id_user':f[0], 'username':f[1],
                   'email':f[2], 'password':f[3],
                   'birthdate':f[4], 'nationality':f[5]}
            usrs.append(usr)
        print(dato)
        return jsonify({'users': usrs, 'msg': 'users founded'})
        # return "table founded!"
    except Exception as ex:
        return "Error"

@app.route('/users/<usr>', methods=['GET'])
def get_user(usr):
    try:
        cur = cnx.connection.cursor()
        sql = "SELECT * FROM users WHERE username = '{0}' ".format(usr)
        cur.execute(sql)
        d = cur.fetchone()
        if d != None:
            usr = {'id_user': d[0], 'username': d[1],
                   'email': d[2], 'password': d[3],
                   'birthdate': d[4], 'nationality': d[5]}
            return jsonify({'user': usr, 'msg': "user founded"})
        else:
            return jsonify({"msg": "Error: user not founded"})
    except Exception as ex:
        return jsonify({"msg": "Error getting user"})


@app.route('/users', methods=['POST'])
def register_user():
    try:
        cur = cnx.connection.cursor()
        sql = "INSERT INTO users(username, email, password, birthdate, nationality) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['user'], request.json['email'],
                                                                     request.json['password'], request.json['birthdate'],
                                                                     request.json['nationality'])
        cur.execute(sql)
        cnx.connection.commit() # commit the transaction
        return jsonify({'msg': 'Successfully registered'})
    except Exception as ex:
        return jsonify({"msg": "Error registering user"})


@app.route('/users/<usr>', methods=['PUT'])
def update_user(usr):
    try:
        cur = cnx.connection.cursor()
        sql = "UPDATE users SET password ='{0}', nationality ='{1}' WHERE email = '{2}'".format(request.json['password'],
                                                                                                request.json['nationality'],
                                                                                                usr)
        cur.execute(sql)
        cnx.connection.commit() # commit the transaction
        return jsonify({'msg': 'Successfully modified user'})
    except Exception as ex:
        return jsonify({"msg": "Error modifying user"})


@app.route('/users/<usr>', methods=['DELETE'])
def delete_user(usr):
    try:
        cur = cnx.connection.cursor()
        sql = "DELETE FROM users WHERE email = '{0}'".format(usr)
        cur.execute(sql)
        cnx.connection.commit()  # commit the transaction
        return jsonify({'msg': 'User deleted successfully'})
    except Exception as ex:
        return jsonify({"msg": "Error: cannot drop the whole table:C"})
def page_not_found(error):
    return render_template('not_steph.html'), 404

@app.errorhandler(404)
def not_found(error):
    return render_template('not_steph.html'), 404

if __name__ == '__main__':
    # conda activate RestApi
    # db.execSQL("CREATE TABLE users(username text PRIMARY KEY, email text, password text, birthdate text, nacion text)");
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
    