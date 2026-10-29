from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = []
id = 0

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    global id
    id = id + 1
    dados = request.get_json()
    aluno = {
        "id": id,
        "nome": dados.get("nome"),
        "curso": dados.get("curso"),
        "idade": dados.get("idade")
    }
    alunos.append(aluno)
    return jsonify(aluno)

app.run(debug=True)