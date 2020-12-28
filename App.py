from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask
from flask_mysqldb import MySQL
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import pyodbc

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ventaproductos'
mysql = MySQL(app)
db = SQLAlchemy(app)


pyodbc.drivers()
# SQLServer
Server = 'sql5063.site4now.net'
Driver = 'ODBC Driver 17 for SQL Server'
Database = 'DB_A6C1FF_HikingGuanacaste'
Username = 'DB_A6C1FF_HikingGuanacaste_admin'
Password = 'Qy*rDC5cq.3u9ei'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql5063.site4now.net;DATABASE=DB_A6C1FF_HikingGuanacaste;UID=DB_A6C1FF_HikingGuanacaste_admin;PWD=Evaristo1992')

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql5063.site4now.net;DATABASE=DB_A6C1FF_HikingGuanacaste;UID=DB_A6C1FF_HikingGuanacaste_admin;PWD=Evaristo1992')


# settings
app.secret_key = "mysecretkey"


# routes


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', products=data)


@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04')
    data = cur.fetchall()
    cur.execute('SELECT * FROM in05')
    data2 = cur.fetchall()
    cur.close()
    return render_template('home.html', products=data, familys=data2)


@app.route('/indexB')
def indexB():

    return render_template('indexB.html')


@app.route('/Error')
def Error():

    return render_template('Error.html')


@app.route('/index2')
def Index2():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM in04')
    data = cursor.fetchall()
    cursor.close()
    return render_template('index2.html', products=data)


@app.route('/family')
def family():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in05')
    data = cur.fetchall()
    cur.close()
    return render_template('family.html', familys=data)


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        CodigoProducto = request.form['CodigoProducto']
        Precio = request.form['Precio']
        SaldoInventario = request.form['SaldoInventario']
        FechaIngreso = request.form['FechaIngreso']
        UsuarioIngreso = request.form['UsuarioIngreso']
        IDFamilia = request.form['IDFamilia']
        Descripcion = request.form['Descripcion']
        NombreProduto = request.form['NombreProduto']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO in04 (CodigoProducto,Precio,SaldoInventario,FechaIngreso,UsuarioIngreso,IDFamilia,Descripcion,NombreProduto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (CodigoProducto, Precio, SaldoInventario, FechaIngreso, UsuarioIngreso, IDFamilia, Descripcion, NombreProduto))
        mysql.connection.commit()
        flash('Registro Exitoso!!')
        return redirect(url_for('Index'))


@app.route('/add_family', methods=['POST'])
def add_family():
    if request.method == 'POST':
        IDFamilia = request.form['IDFamilia']
        NombreFamilia = request.form['NombreFamilia']
        UsuarioIngreso = request.form['UsuarioIngreso']
        Estado = request.form['Estado']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO in05 (IDFamilia,NombreFamilia,UsuarioIngreso,Estado) VALUES (%s,%s,%s,%s)",
                    (IDFamilia, NombreFamilia, UsuarioIngreso, Estado))
        mysql.connection.commit()
        flash('Registro Exitoso!!')
        return redirect(url_for('family'))


@app.route('/add_productsql', methods=['POST'])
def add_productsql():
    if request.method == 'POST':
        CodigoProducto = request.form['CodigoProducto']
        Precio = request.form['Precio']
        SaldoInventario = request.form['SaldoInventario']
        FechaIngreso = request.form['FechaIngreso']
        UsuarioIngreso = request.form['UsuarioIngreso']
        IDFamilia = request.form['IDFamilia']
        Descripcion = request.form['Descripcion']
        cursor = conn.cursor()
        cursor.execute("INSERT INTO in04 (CodigoProducto,Precio,SaldoInventario,FechaIngreso,UsuarioIngreso,IDFamilia,Descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       (CodigoProducto, Precio, SaldoInventario, FechaIngreso, UsuarioIngreso, IDFamilia, Descripcion))
        cnxn.commit()
        flash('Registro Exitoso!!')

        return redirect(url_for('Index2'))


@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04 WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-product.html', product=data[0])


@app.route('/detalle/<id>', methods=['POST', 'GET'])
def get_product(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04 WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('detalle-product.html', product=data[0])


@app.route('/detallefamily/<id>', methods=['POST', 'GET'])
def get_family(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04 WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('detalle-family.html', family=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        CodigoProducto = request.form['CodigoProducto']
        Precio = request.form['Precio']
        SaldoInventario = request.form['SaldoInventario']
        FechaIngreso = request.form['FechaIngreso']
        UsuarioIngreso = request.form['UsuarioIngreso']
        IDFamilia = request.form['IDFamilia']
        Descripcion = request.form['Descripcion']
        NombreProduto = request.form['NombreProduto']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE in04
            SET 
        CodigoProducto  = %s,
        Precio  = %s,
        SaldoInventario = %s,
        FechaIngreso  = %s,
        UsuarioIngreso  = %s,
        IDFamilia  = %s,
        Descripcion = %s,
        NombreProduto = %s
            WHERE id = %s
        """, (CodigoProducto, Precio, SaldoInventario, FechaIngreso, UsuarioIngreso, IDFamilia, Descripcion, NombreProduto, id))
        flash('Registro Actualizado con exito!!')
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM in04 WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro Eliminado!!')
    return redirect(url_for('Index'))


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
