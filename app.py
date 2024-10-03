from flask import Flask, render_template, request, redirect, abort, jsonify

app = Flask(__name__)

# Rota principal
@app.route("/")
def hello_world():
    return render_template("index.html")

# Rota para o usuário
@app.route("/user/GabrieleBarros")
def user(nome):
    return f"<h1>Hello, {nome.replace('_', ' ')}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# Rota para o contexto da requisição
@app.route("/contextorequisicao")
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return f"Your browser is: {user_agent}"

# Rota para retornar um código de status diferente
@app.route("/codigostatusdiferente")
def codigo_status_diferente():
    return "Bad request", 202

# Rota para retornar um objeto como resposta JSON
@app.route("/objetoresposta")
def objeto_resposta():
    data = {"This document carries a cookie!"}
    return jsonify(data)

# Rota para redirecionamento
@app.route("/redirecionamento")
def redirecionamento():
    return redirect("/https://ptb.ifsp.edu.br/")

# Rota para abortar com um código de erro
@app.route("/abortar")
def abortar():
    abort(404)  # 404 Not Found

if __name__ == "__main__":
    app.run(debug=True)
