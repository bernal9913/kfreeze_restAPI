from crypt import methods

from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from config import config

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'b7e3a09e061e12'
app.config['MYSQL_PASSWORD'] = '2f9d3cc1'
app.config['MYSQL_DB'] = 'heroku_d02c1597b242410'
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/verTabla', methods=['GET'])
def vertabla():
    if request.method == 'GET':
        try:
            cur = mysql.connection.cursor()
            sql = "SELECT * FROM usersBernal "
            cur.execute(sql)
            dato = cur.fetchall()
            return render_template('verTabla.html', data=dato)
        except Exception as e:
            return redirect(url_for('/'))


@app.route('/users', methods=['GET'])
def list_users():
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT idusers, username, password, email, DATE_FORMAT(datebirth, '%d/%m/%Y') as dateBirth, placeOfBirth, userType, firstName, lastName FROM `heroku_d02c1597b242410`.`usersbernal`;"
        cur.execute(sql)
        dato = cur.fetchall()
        usrs = []
        for f in dato:
            usr = {'id_user': f[0], 'username': f[1],
                   'password': f[2], 'email': f[3],
                   'birthdate': f[4], 'nationality': f[5],
                   'userType': f[6], 'firstName': f[7],
                   'lastName': f[8]}
            usrs.append(usr)
        print(dato)
        return jsonify({'users': usrs, 'msg': 'users founded'})
        # return "table founded!"
    except Exception as ex:
        return "Error en query o la vida"


@app.route('/log_user', methods=['POST'])
# login user method
def get_user():
    try:
        cur = mysql.connection.cursor()
        # sql = "SELECT * FROM users WHERE username = '{0}' ".format(usr)
        sql = "SELECT idusers, username, password, email, DATE_FORMAT(datebirth, '%d/%m/%Y') as dateBirth, placeOfBirth, userType, firstName, lastName FROM usersBernal WHERE username = '{0}' AND password = '{1}'".format(
            request.json['user'],
            request.json['password'])
        cur.execute(sql)
        f = cur.fetchone()
        if f != None:
            usr = {'id_user': f[0], 'username': f[1],
                   'password': f[2], 'email': f[3],
                   'birthdate': f[4], 'nationality': f[5],
                   'userType': f[6], 'firstName': f[7],
                   'lastName': f[8]}
            return jsonify({'user': usr, 'msg': "user founded"})
        else:
            return jsonify({'msg': "Error: user not founded"})
    except Exception as ex:
        return jsonify({"msg": "Error getting user"})


@app.route('/users', methods=['POST'])
# Register a user method
def register_user():
    try:
        cur = mysql.connection.cursor()
        #query = "SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE 'username' = '" + request.json['user'] + "'"

        # cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE username = '" + request.json['user'] + "' or email = '" + request.json['email'] + "'")
        cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE username = '" + request.json['user'] + "'")
        check_user = cur.fetchone()
        cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '" + request.json['email'] + "'")
        check_email = cur.fetchone()
        if check_user:
            return jsonify({"msg": "User already registered"})
        if check_email:
            return jsonify({"msg": "Email already registered"})
        if check_user is None and check_email is None:
            # TODO add first and last name
            # TODO trimmear ms
            val = (request.json['user'], request.json['email'],
            request.json['password'], request.json['birthdate'],
            request.json['nationality'], request.json['firstName'],
            request.json['lastName'])
            sql = "INSERT INTO `heroku_d02c1597b242410`.`usersbernal`(username, email, password, datebirth, placeOfBirth, firstName, lastName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            #sql = "INSERT INTO `heroku_d02c1597b242410`.`usersbernal`(username, email, password, datebirth, placeOfBirth, firstName, lastName) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}'), '{5}', '{6}'".format(
            #request.json['user'], request.json['email'],
            #request.json['password'], request.json['birthdate'],
            #request.json['nationality'], request.json['firstName'],
            #request.json['lastName'])
            cur.execute(sql, val)
            mysql.connection.commit()  # commit the transaction
            return jsonify({'msg': 'Successfully registered'})
    except Exception as ex:
        return jsonify({"msg": "Error registering user"})


@app.route('/users', methods=['PUT'])
# update password for user account
def update_user():
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '" + request.json['email'] + "'")
        check_user = cur.fetchone()
        if check_user:
            sql = "UPDATE `heroku_d02c1597b242410`.`usersbernal` SET password ='{1}' WHERE email = '{0}'".format(
                request.json['email'],
                request.json['password'])
            cur.execute(sql)
            mysql.connection.commit()  # commit the transaction
            return jsonify({'msg': 'Successfully modified user'})
        else:
            return jsonify({'msg': 'user not found'})
    except Exception as ex:
        return jsonify({"msg": "Error modifying user"})

@app.route('/users/mouseketools', methods=['POST'])
def shh():
    try:
        if request.json['password'] == 'ClaveBelica':
            cur = mysql.connection.cursor()
            #cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '" + request.json['email'] + "'")
            check_user = cur.fetchone()
            if check_user:
                sql = "UPDATE `heroku_d02c1597b242410`.`usersbernal` SET userType ='Admin' WHERE email = '{0}'".format(
                request.json['email'])
                cur.execute(sql)
                mysql.connection.commit() # commit the transaction
                return jsonify({'msg': 'Successfully upgraded user'})
            else:
                return jsonify({'msg': 'User not found'})
        else:
            return jsonify({"msg": 'Admin password is incorrect'})
    except Exception as ex:
        return jsonify({"msg": "Error making upgrading user"})
@app.route('/users/demote', methods=['POST'])
def demote():
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '" + request.json['email'] + "'")
        check_user = cur.fetchone()
        if check_user:
        #cur = mysql.connection.cursor()
            sql = "UPDATE `heroku_d02c1597b242410`.`usersbernal` SET userType ='Regular' WHERE email = '{0}'".format(
                request.json['email'])
            cur.execute(sql)
            mysql.connection.commit() # commit the transaction
            return jsonify({'msg': 'Successfully downgraded user'})
        else:
            return jsonify({'msg': 'User not found'})
    except Exception as ex:
        return jsonify({"msg": "Error making upgrading user"})
@app.route('/users/', methods=['DELETE'])
def delete_user():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '" + request.json['email'] + "'")
        check_user = cur.fetchone()
        if check_user:
            sql = "DELETE FROM `heroku_d02c1597b242410`.`usersbernal` WHERE email = '{0}'".format(
                request.json['email'])
            cur.execute(sql)
            mysql.connection.commit()  # commit the transaction
            return jsonify({'msg': 'User deleted successfully'})
        else:
            return jsonify({'msg': 'User not founded'})
    except Exception as ex:
        return jsonify({"msg": "Error: cannot drop the whole table:C"})

@app.route('/dpbernal/add', methods=['POST'])
def addphoto():
    try:
        cur = mysql.connection.cursor()
        sql = "INSERT INTO `heroku_d02c1597b242410`.`dpbernal`(user, photo) VALUES (%s, %s)"
        val = (request.json['user'], request.json['photo'])
        cur.execute(sql, val)
        mysql.connection.commit()
        return jsonify({"msg":"success"})
    except Exception as ex:
        return jsonify({"msg":"error"})

@app.route('/dpbernal/mod', methods=['POST'])
def modphoto():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`dpbernal` WHERE user = %s", request.json['user'])
        check_user = cur.fetchone()
        if check_user:
            sql = "update `heroku_d02c1597b242410`.`dpbernal` set photo = '{0}' where user = '{1}'".format(request.json['photo'],request.json['user'])
            cur.execute(sql)
            mysql.connection.commit()
            return jsonify({"msg": "success"})
        else:
            return jsonify({"msg": "error finding user"})
    except Exception as e:
        return jsonify({"msg":"error updating photo"})

@app.route("/dpbernal/check", methods=['POST'])
def checkPhoto():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `heroku_d02c1597b242410`.`dpbernal` WHERE user = '" + request.json['user'] + "'")
        #cur.execute(sql)
        check = cur.fetchone()
        if check != None:
            usr = {'id_photo': check[0], 'username': check[1],
                   'photo': check[2]}
            return jsonify({'user': usr, 'msg': "user founded"})
        else:
            return jsonify({"msg":"no photo available"})
    except Exception as e:
        return jsonify({"msg": "Error on db "})
def page_not_found(error):
    return render_template('not_steph.html'), 404

@app.errorhandler(404)
def not_found(error):
    return render_template('not_steph.html'), 404

# uncomment those lines for local testing purposes
#if __name__ == '__main__':
#    app.run(debug=True)