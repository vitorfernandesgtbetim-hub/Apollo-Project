from flask import Flask, app, request, jsonify
from models import Profissional

app = Flask(__name__)

# CADASTRO DE PROFISSIONAL

@app.route('/api/profissional', methods=['POST'])

def cadastrar_profissional():
    dados = request.get_json()
    prof = Profissional(dados['nome'], dados['cpf'], dados['telefone'], dados['email'], dados['cargo'], dados['especialidade'], dados['status'])

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO profissional (nome, cpf, telefone, email, cargo, especialidade, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (prof.nome, prof.cpf, prof.telefone, prof.email, prof.cargo, prof.especialidade, prof.status))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Profissional cadastrado com sucesso!"}), 201


# EXCLUSÃO DE PROFISSIONAL

@app.route('/api/profissional/<int:id_profissional>', methods=['DELETE'])

def deletar_profissional(id_profissional):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profissional WHERE id_profissional = %s", (id_profissional,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Profissional deletado com sucesso!"}), 200


# ATUALIZAÇÃO DE PROFISSIONAL

@app.route('/api/profissional/<int:id_profissional>', methods=['PUT'])

def atualizar_profissional(id_profissional):
    dados = request.get_json()
    prof = Profissional(id_profissional, dados['nome'], dados['cpf'], dados['telefone'], dados['email'], dados['cargo'], dados['especialidade'], dados['status'])
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE profissional SET nome = %s, cpf = %s, telefone = %s, email = %s, cargo = %s, especialidade = %s, status = %s WHERE id_profissional = %s"
    cursor.execute(sql, (prof.nome, prof.cpf, prof.telefone, prof.email, prof.cargo, prof.especialidade, prof.status, prof.id_profissional))
    conn.commit()
    cursor.close()
    conn.close()   

    return jsonify({"message": "Profissional atualizado com sucesso!"}), 200



# ROTA DE BUSCA DE FUNCIONÁRIOS COM FILTRO

@app.route('/api/profissional', methods=['GET'])

def buscar_funcionarios():
    nome = request.args.get('nome')
    cargo = request.args.get('cargo')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM profissional WHERE 1=1"

    params = []

    if nome:
        sql += " AND nome LIKE %s"
        params.append(f"%{nome}%")

    if cargo:
        sql += " AND cargo LIKE %s"
        params.append(f"%{cargo}%")

    cursor.execute(sql, params)
    funcionarios = cursor.fetchall()
    cursor.close() 
    conn.close()

    return jsonify(funcionarios), 200

    

    