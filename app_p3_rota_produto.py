from flask import Flask, app, request, jsonify
from models import Produto

app = Flask(__name__)


# ROTA DE ADIÇÃO DE PRODUTO

@app.route('/api/produtos', methods=['POST'])

def cadastrar_produto():
    dados = request.get_json()
    produto = Produto(dados['nome'], dados['descricao'], dados['categoria'], dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidad_minima'])

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO produtos (nome, descricao, categoria, unidade_medida, quantidade_estoque, quantidad_minima) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (produto.nome, produto.descricao, produto.categoria, produto.unidade_medida, produto.quantidade_estoque, produto.quantidad_minima))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201


# ROTA DE EXCLUSÃO DE PRODUTO

@app.route('/api/produtos/<int:id_produto>', methods=['DELETE'])

def excluir_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id_produto = %s", (id_produto,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto excluído com sucesso!"}), 200



# ROTA DE EDIÇÃO/ATUALIZAÇÃO DE PRODUTO

@app.route('/api/produtos/<int:id_produto>', methods=['PUT'])

def atualizar_produto(id_produto):
    dados = request.get_json()
    produto = Produto(dados['nome'], dados['descricao'], dados['categoria'], dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidad_minima'])
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE produtos SET nome = %s, descricao = %s, categoria = %s, unidade_medida = %s, quantidade_estoque = %s, quantidad_minima = %s WHERE id_produto = %s"
    cursor.execute(sql, (produto.nome, produto.descricao, produto.categoria, produto.unidade_medida, produto.quantidade_estoque, produto.quantidad_minima, id_produto))
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
    cursor = conn.cursor(dictory=True)
    sql = "SELECT * FROM produtos WHERE 1=1"
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




