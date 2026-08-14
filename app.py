from flask import Flask, request, jsonify
from models import Profissional, Cliente, Produto

app = Flask(__name__)

# ==========================================
# 1. ROTAS DE PROFISSIONAL
# ==========================================

# CADASTRO DE PROFISSIONAL
@app.route('/api/profissional', methods=['POST'])
def cadastrar_profissional():
    dados = request.get_json()
    prof = Profissional(
        dados['nome'], dados['cpf'], dados['telefone'], 
        dados['email'], dados['cargo'], dados['especialidade'], dados['status']
    )

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
    prof = Profissional(
        id_profissional, dados['nome'], dados['cpf'], dados['telefone'], 
        dados['email'], dados['cargo'], dados['especialidade'], dados['status']
    )
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


# ==========================================
# 2. ROTAS DE CLIENTE
# ==========================================

# CADASTRO DE CLIENTE
@app.route('/api/cliente', methods=['POST'])
def cadastrar_cliente():
    dados = request.get_json()
  
    clien = Cliente(
        dados['nome'], dados['cpf'], dados['telefone'], dados['email'], 
        dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], 
        dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO cliente (nome, cpf, telefone, email, data_nascimento, cep, rua, numero, bairro, cidade, estado, data_cadastro, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (
        clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, 
        clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, 
        clien.data_cadastro, clien.status
    ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201


# EXCLUSÃO DE CLIENTE
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
    clien = Cliente(
        dados['nome'], dados['cpf'], dados['telefone'], dados['email'], 
        dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], 
        dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, email = %s, data_nascimento = %s, cep = %s, rua = %s, numero = %s, bairro = %s, cidade = %s, estado = %s, data_cadastro = %s, status = %s WHERE id_cliente = %s"
    cursor.execute(sql, (
        clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, 
        clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, 
        clien.data_cadastro, clien.status, id_cliente
    ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200


# ROTA DE BUSCA DE CLIENTES COM FILTRO
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


# ==========================================
# 3. ROTAS DE PRODUTO
# ==========================================

# ROTA DE ADIÇÃO DE PRODUTO
@app.route('/api/produtos', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()
    produto = Produto(
        dados['nome'], dados['descricao'], dados['categoria'], 
        dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidade_minima']
    )

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO produto (nome, descricao, categoria, unidade_medida, quantidade_estoque, quantidade_minima) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (
        produto.nome, produto.descricao, produto.categoria, 
        produto.unidade_medida, produto.quantidade_estoque, produto.quantidade_minima
    ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201


# ROTA DE EXCLUSÃO DE PRODUTO
@app.route('/api/produtos/<int:id_produto>', methods=['DELETE'])
def excluir_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Corrigido tabela 'produtos' -> 'produto'
    cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto excluído com sucesso!"}), 200


# ROTA DE EDIÇÃO/ATUALIZAÇÃO DE PRODUTO
@app.route('/api/produtos/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    dados = request.get_json()
    produto = Produto(
        dados['nome'], dados['descricao'], dados['categoria'], 
        dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidade_minima']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE produto SET nome = %s, descricao = %s, categoria = %s, unidade_medida = %s, quantidade_estoque = %s, quantidade_minima = %s WHERE id_produto = %s"
    cursor.execute(sql, (
        produto.nome, produto.descricao, produto.categoria, 
        produto.unidade_medida, produto.quantidade_estoque, produto.quantidade_minima, id_produto
    ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto atualizado com sucesso!"}), 200


# ROTA DE BUSCA DE PRODUTOS COM FILTROS
@app.route('/api/produtos', methods=['GET'])
def buscar_produtos():
    nome = request.args.get('nome')
    categoria = request.args.get('categoria')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE 1=1"
    params = []

    if nome:
        sql += " AND nome LIKE %s"
        params.append(f"%{nome}%")

    if categoria:
        sql += " AND categoria = %s"
        params.append(categoria)

    cursor.execute(sql, tuple(params))
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(produtos), 200
