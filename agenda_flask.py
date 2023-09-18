from flask import Flask, render_template, request, redirect, url_for
import uuid
import os

app = Flask(__name__)

caminho_absoluto = os.path.abspath("login.txt")

def verificar_login(username, password):
    with open(caminho_absoluto, 'r') as file:
        for line in file:
            cadastro= line.strip().split('-')
            if username == cadastro[0] and password == cadastro[1]:
                return True
    return False


@app.route("/", methods = ['GET','POST'])
def formulario():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if verificar_login(usuario, senha):
            return redirect(url_for('carta'))
        
        else:
            return "<h1>USUARIO / SENHA INVALIDOS<h1>"
            
    return render_template('login.html')    

@app.route("/carta", methods = ['GET','POST'] )
def carta():
    if request.method == 'POST':
        data = request.form.get("data")
        destinatario = request.form.get("destinatario")
        mensagem = request.form.get("mensagem")
        remetente = request.form.get("remetente")
        nome_arquivo = f'carta_cod_{str(uuid.uuid4())}.txt'
    
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(data + '\n')
            arquivo.write(destinatario + '\n')
            arquivo.write(mensagem + '\n')
            arquivo.write(remetente + '\n')
        
        return render_template('carta.html')

    return render_template('carta.html')



app.run()
