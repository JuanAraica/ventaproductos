from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ventaproductos'
mysql = MySQL(app)


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
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO in04 (CodigoProducto,Precio,SaldoInventario,FechaIngreso,UsuarioIngreso,IDFamilia,Descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (CodigoProducto, Precio, SaldoInventario, FechaIngreso, UsuarioIngreso, IDFamilia, Descripcion))
        mysql.connection.commit()
        flash('Registro Exitoso!!')
        return redirect(url_for('Index'))


@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04 WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-product.html', product=data[0])


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
        Descripcion = %s
            WHERE id = %s
        """, (CodigoProducto, Precio, SaldoInventario, FechaIngreso, UsuarioIngreso, IDFamilia, Descripcion, id))
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
