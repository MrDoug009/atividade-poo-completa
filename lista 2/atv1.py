from flask import Flask, request, jsonify

app = Flask(__name__)

filmes = []

@app.route('/filmes/<int:id>', methods=['PUT'])
def atualizar_filme(id):
    dados = request.get_json()
    for filme in filmes:
        if filme["id"] == id:
            filme["nome"] = dados.get("nome")
            filme["diretor"] = dados.get("diretor")
            filme["ano"] = dados.get("ano")
            return jsonify(filme)
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route('/filmes/<int:id>', methods=['DELETE'])
def deletar_filme(id):
    global filmes
    filmes = [filme for filme in filmes if filme["id"] != id]
    return jsonify({"mensagem": "Filme removido com sucesso"}), 200

app.run(debug=True)