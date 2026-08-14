from flask import Flask, app, request, jsonify
from models import Cliente

app = Flask(__name__)

# CADASTRO DE CLIENTE

@app.route('/api/cliente', methods=['POST'])

def cadastrar_cliente():
    dados = request.get_json()

    clien = Cliente(dados['nome'], dados['cpf'], dados['telefone'], dados['email'], dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status'], dados['observacoes'])
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO cliente (nome, cpf, telefone, email, data_nascimento, cep, rua, numero, bairro, cidade, estado, data_cadastro, status, observacoes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, clien.data_cadastro, clien.status, clien.observacoes))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201


# EXCLUSÃO DE PROFISSIONAL

@app.route('/api/cliente/<int:id_cliente>', methods=['DELETE'])

def excluir_cliente(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente excluído com sucesso!"}), 200



# ATUALIZAÇÃO DE CLIENTE

@app.route('/api/cliente/<int:id_cliente>', methods=['PUT'])

def atualizar_cliente(id_cliente):
    dados = request.get_json()
    clien = Cliente(dados['nome'], dados['cpf'], dados['telefone'], dados['email'], dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status'], dados['observacoes'])
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, email = %s, data_nascimento = %s, cep = %s, rua = %s, numero = %s, bairro = %s, cidade = %s, estado = %s, data_cadastro = %s, status = %s, observacoes = %s WHERE id_cliente = %s"
    cursor.execute(sql, (clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, clien.data_cadastro, clien.status, clien.observacoes, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200


@app.route('/api/cliente', methods=['GET'])
def buscar_clientes():
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    telefone = request.args.get('telefone')
    email = request.args.get('email')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM cliente WHERE 1=1"
    params = []

    if nome:
        sql += " AND nome LIKE %s"
        params.append(f"%{nome}%")

    if cpf:
        sql += " AND cpf LIKE %s"
        params.append(f"%{cpf}%")

    if telefone:
        sql += " AND telefone LIKE %s"
        params.append(f"%{telefone}%")

    if email:
        sql += " AND email LIKE %s"
        params.append(f"%{email}%")

    cursor.execute(sql, tuple(params))
    clientes = cursor.fetchall()
    cursor.close()  
    conn.close()

    return jsonify(clientes), 200

