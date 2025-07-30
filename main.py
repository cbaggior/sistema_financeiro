from flask import Flask, jsonify, request

app = Flask(__name__)
tarefas = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Tarefas funcionando!"})

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nova = request.get_json()
    tarefas.append(nova)
    return jsonify(nova), 201

if __name__ == "__main__":
    app.run(debug=True)
