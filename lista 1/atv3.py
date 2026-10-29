from flask import Flask, request, jsonify

app = Flask(__name__)

musicas = []
id = 0

@app.route('/musicas', methods=['POST'])
def criar_musica():
    global id
    id = id + 1
    dados = request.get_json()
    musica = {
        "id": id,
        "nome": dados.get("nome"),
        "artista": dados.get("artista"),
        "ano": dados.get("ano")
    }
    musicas.append(musica)
    return jsonify(musica)

app.run(debug=True)