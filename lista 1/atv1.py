from flask import Flask, request, jsonify

app = Flask(__name__)

filmes = []
id = 0

@app.route('/filmes', methods=['POST'])
def criar_filme():
    global id
    id = id + 1
    dados = request.get_json()
    filme = {
        "id": id,
        "nome": dados.get("nome"),
        "diretor": dados.get("diretor"),
        "ano": dados.get("ano")
    }
    filmes.append(filme)
    return jsonify(filme)

app.run(debug=True)