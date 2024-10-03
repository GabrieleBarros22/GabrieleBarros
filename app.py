from flask import Flask, render_template, request, redirect, abort, jsonify

app = Flask(__name__)

# Rota principal
@app.route("/")
def hello_world():
    return render_template("index.html")

# Rota para o usuário
@app.route("/user/<name>")
def user(name):
    return f"Olá, {name}!"

# Rota para o contexto da requisição
@app.route("/contextorequisicao")
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return f"Seu User-Agent é: {user_agent}"

# Rota para retornar um código de status diferente
@app.route("/codigostatusdiferente")
def codigo_status_diferente():
    return "Este é um código de status diferente!", 202

# Rota para retornar um objeto como resposta JSON
@app.route("/objetoresposta")
def objeto_resposta():
    data = {"message": "Esta é uma resposta JSON", "status": 200}
    return jsonify(data)

# Rota para redirecionamento
@app.route("/redirecionamento")
def redirecionamento():
    return redirect("/")

# Rota para abortar com um código de erro
@app.route("/abortar")
def abortar():
    abort(403)  # 403 Forbidden

if __name__ == "__main__":
    app.run(debug=True)
