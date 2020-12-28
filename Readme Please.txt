Tecnologias implementadas:
Back-End:
Python 3.9
Pip 20.2.3
SQl Server 
Pyodbc 
SQLAlchemy
pandas

From-End:
Html 5 y Jinja 2
CSS
Bootswatch




Metodologia:
Programacion horientada a Objetos.

Repositorio GitHub:
https://github.com/JuanAraica/ventaproductos.git



    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM in04')
    data = cur.fetchall()
    cur.close()


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ventaproductos'
mysql = MySQL(app)