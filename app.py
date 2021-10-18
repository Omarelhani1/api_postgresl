import os
from flask import Flask, render_template,abort,request
import psycopg2
app = Flask(__name__)	

@app.route('/',methods=["GET"])
def login():
    return render_template("login.html")

@app.route('/psql',methods=["POST"])
def postgres():
    bd=request.form.get("d")
    u=request.form.get("u")
    p=request.form.get("p")
    conexion=psycopg2.connect(host="192.168.122.3",database=bd,user="root",password="omar")
    cur = conexion.cursor()
    lista_tablas=['medicos','pacientes','horasdeconsulta','salasdeconsultas']
    lista_columnas=[]
    for a in lista_tablas:
        cur.execute("select column_name from information_schema.columns where table_name='%s';" % a)
        lista=[]
        for a in cur.fetchall():
            lista.append(str(a))
        lista_columnas.append(lista)
    lista_resultados=[]
    for a in lista_tablas:
        cur.execute("select * from %s;" % a)
        lista=[]
        for a in cur.fetchall():
            lista.append(a)
        lista_resultados.append(lista)
    return render_template("psql.html",d=d,lista_tablas=lista_tablas,lista_columnas=lista_columnas,num=len(lista_tablas),lista_resultados=lista_resultados)


port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)