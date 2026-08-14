# Importação dos módulos necessários do Flask
from flask import Flask, request, jsonify

# Importação do driver de conexão com o banco de dados MySQL
import mysql.connector

# Importação das classes Models do arquivo models.py
from models import Profissional, Cliente, Produto, Consulta, Movimentacao_estoque, Feedback

# Inicialização da aplicação Flask
app = Flask(__name__)

# ==========================================
# FUNÇÃO AUXILIAR DE CONEXÃO COM O BANCO
# ==========================================
def get_db_connection():
    # Estabelece e retorna a conexão com o banco MySQL 'dba_apolo'
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # Insira a senha do seu MySQL se houver
        database="dba_apolo"
    )

# ==========================================
# 1. ROTAS DE PROFISSIONAL
# ==========================================

# ROTA PARA CADASTRAR NOVO PROFISSIONAL
@app.route('/api/profissional', methods=['POST'])
def cadastrar_profissional():
    # Obtém os dados no formato JSON enviados no corpo da requisição
    dados = request.get_json()
    
    # Instancia a classe Profissional para estruturar os dados recebidos
    prof = Profissional(
        dados['nome'], dados['cpf'], dados['telefone'], 
        dados['email'], dados['cargo'], dados['especialidade'], dados['status']
    )

    # Abre a conexão com o banco de dados
    conn = get_db_connection()
    # Cria o cursor para executar as instruções SQL
    cursor = conn.cursor()

    # Prepara a query SQL parametrizada com %s para evitar SQL Injection
    sql = """INSERT INTO profissional (nome, cpf, telefone, email, cargo, especialidade, status) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
             
    # Executa a instrução SQL passando os dados obtidos da model Profissional
    cursor.execute(sql, (prof.nome, prof.cpf, prof.telefone, prof.email, prof.cargo, prof.especialidade, prof.status))
    
    # Confirma as alterações permanentemente no banco de dados
    conn.commit()
    
    # Fecha o cursor e a conexão para liberar memória no servidor
    cursor.close()
    conn.close()

    # Retorna uma mensagem de sucesso em formato JSON com código HTTP 201 (Created)
    return jsonify({"message": "Profissional cadastrado com sucesso!"}), 201


# ROTA PARA BUSCAR PROFISSIONAIS COM FILTROS OPCIONAIS
@app.route('/api/profissional', methods=['GET'])
def buscar_funcionarios():
    # Captura os parâmetros de busca passados via URL Query String (ex: ?nome=Ana&cargo=Medico)
    nome = request.args.get('nome')
    cargo = request.args.get('cargo')
    
    # Abre a conexão com o banco
    conn = get_db_connection()
    # O parâmetro dictionary=True faz o MySQL retornar os dados como dicionário Python (chave: valor)
    cursor = conn.cursor(dictionary=True)

    # SQL base usando o truque 'WHERE 1=1' para permitir encadear filtros 'AND' dinamicamente
    sql = "SELECT * FROM profissional WHERE 1=1"
    params = []

    # Se o parâmetro 'nome' foi enviado na URL, adiciona o filtro na consulta SQL
    if nome:
        sql += " AND nome LIKE %s"
        params.append(f"%{nome}%")

    # Se o parâmetro 'cargo' foi enviado na URL, adiciona o filtro na consulta SQL
    if cargo:
        sql += " AND cargo LIKE %s"
        params.append(f"%{cargo}%")

    # Executa o SQL passando a tupla de parâmetros compilados dinamicamente
    cursor.execute(sql, tuple(params))
    
    # Busca todos os registros correspondentes retornados da consulta
    funcionarios = cursor.fetchall()
    
    # Encerra o cursor e a conexão
    cursor.close() 
    conn.close()

    # Converte a lista de resultados em JSON e retorna com HTTP status 200 (OK)
    return jsonify(funcionarios), 200


# ROTA PARA ATUALIZAR UM PROFISSIONAL EXISTENTE
@app.route('/api/profissional/<int:id_profissional>', methods=['PUT'])
def atualizar_profissional(id_profissional):
    # Captura o JSON enviado na requisição com os dados atualizados
    dados = request.get_json()
    
    # Instancia o objeto Profissional repassando os novos dados
    prof = Profissional(
        dados['nome'], dados['cpf'], dados['telefone'], 
        dados['email'], dados['cargo'], dados['especialidade'], dados['status']
    )
    
    # Conecta ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL de atualização dos dados selecionando pelo ID
    sql = """UPDATE profissional SET 
                nome = %s, cpf = %s, telefone = %s, email = %s, 
                cargo = %s, especialidade = %s, status = %s 
             WHERE id_profissional = %s"""
             
    # Executa o UPDATE repassando os atributos do objeto mais o id_profissional do WHERE
    cursor.execute(sql, (
        prof.nome, prof.cpf, prof.telefone, prof.email, 
        prof.cargo, prof.especialidade, prof.status, id_profissional
    ))
    
    # Confirma as alterações e fecha a conexão
    conn.commit()
    cursor.close()
    conn.close()    

    # Retorna o status de sucesso da atualização
    return jsonify({"message": "Profissional atualizado com sucesso!"}), 200


# ROTA PARA EXCLUIR UM PROFISSIONAL
@app.route('/api/profissional/<int:id_profissional>', methods=['DELETE'])
def deletar_profissional(id_profissional):
    # Conecta ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Executa a exclusão filtrando diretamente pelo ID do profissional recebido pela URL
    cursor.execute("DELETE FROM profissional WHERE id_profissional = %s", (id_profissional,))
    
    # Confirma a deleção e encerra recursos de conexão
    conn.commit()
    cursor.close()
    conn.close()

    # Retorna mensagem confirmando a exclusão
    return jsonify({"message": "Profissional deletado com sucesso!"}), 200


# ==========================================
# 2. ROTAS DE CLIENTE
# ==========================================

# ROTA PARA CADASTRAR NOVO CLIENTE
@app.route('/api/cliente', methods=['POST'])
def cadastrar_cliente():
    # Obtém o payload em formato JSON enviado no corpo da requisição
    dados = request.get_json()
  
    # Instancia a model Cliente
    clien = Cliente(
        dados['nome'], dados['cpf'], dados['telefone'], dados['email'], 
        dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], 
        dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status']
    )
    
    # Conecta ao banco
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Instrução SQL de inserção
    sql = """INSERT INTO cliente (nome, cpf, telefone, email, data_nascimento, cep, rua, numero, bairro, cidade, estado, data_cadastro, status) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
             
    # Executa o comando SQL enviando a tupla com os valores do objeto Cliente
    cursor.execute(sql, (
        clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, 
        clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, 
        clien.data_cadastro, clien.status
    ))
    
    # Persiste os dados e fecha o banco
    conn.commit()
    cursor.close()
    conn.close()

    # Retorna resposta JSON + HTTP 201
    return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201


# ROTA PARA BUSCAR CLIENTES COM FILTROS OPCIONAIS
@app.route('/api/cliente', methods=['GET'])
def buscar_clientes():
    # Captura eventuais query params passados na requisição
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    telefone = request.args.get('telefone')
    email = request.args.get('email')

    # Abre a conexão com o banco solicitando dicts como resposta
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Prepara o SQL dinâmico
    sql = "SELECT * FROM cliente WHERE 1=1"
    params = []

    # Adiciona clausulas AND conforme a existência de parâmetros de busca
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

    # Executa a busca parametrizada
    cursor.execute(sql, tuple(params))
    clientes = cursor.fetchall()
    
    # Libera os recursos
    cursor.close()  
    conn.close()

    # Retorna o array de clientes em JSON
    return jsonify(clientes), 200


# ROTA PARA ATUALIZAR UM CLIENTE
@app.route('/api/cliente/<int:id_cliente>', methods=['PUT'])
def atualizar_cliente(id_cliente):
    # Obtém dados atualizados do corpo da requisição
    dados = request.get_json()
    
    # Instancia o objeto Cliente
    clien = Cliente(
        dados['nome'], dados['cpf'], dados['telefone'], dados['email'], 
        dados['data_nascimento'], dados['cep'], dados['rua'], dados['numero'], 
        dados['bairro'], dados['cidade'], dados['estado'], dados['data_cadastro'], dados['status']
    )
    
    # Abre a conexão
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Instrução UPDATE cobrindo os atributos do cliente
    sql = """UPDATE cliente SET 
                nome = %s, cpf = %s, telefone = %s, email = %s, data_nascimento = %s, 
                cep = %s, rua = %s, numero = %s, bairro = %s, cidade = %s, estado = %s, 
                data_cadastro = %s, status = %s 
             WHERE id_cliente = %s"""
             
    # Executa o comando passando a tupla de valores + id_cliente
    cursor.execute(sql, (
        clien.nome, clien.cpf, clien.telefone, clien.email, clien.data_nascimento, 
        clien.cep, clien.rua, clien.numero, clien.bairro, clien.cidade, clien.estado, 
        clien.data_cadastro, clien.status, id_cliente
    ))
    
    # Confirma alterações e encerra o banco
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200


# ROTA PARA EXCLUIR CLIENTE
@app.route('/api/cliente/<int:id_cliente>', methods=['DELETE'])
def excluir_cliente(id_cliente):
    # Conecta no banco
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Executa o DELETE
    cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
    
    # Confirma e limpa a conexão
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Cliente excluído com sucesso!"}), 200


# ==========================================
# 3. ROTAS DE PRODUTO
# ==========================================

# ROTA PARA ADICIONAR NOVO PRODUTO
@app.route('/api/produtos', methods=['POST'])
def cadastrar_produto():
    # Obtém os dados transmitidos no JSON da requisição
    dados = request.get_json()
    
    # Instancia a classe Produto
    produto = Produto(
        dados['nome'], dados['descricao'], dados['categoria'], 
        dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidade_minima']
    )

    # Abre conexão
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL INSERT direcionado à tabela singular 'produto' do MySQL
    sql = """INSERT INTO produto (nome, descricao, categoria, unidade_medida, quantidade_estoque, quantidade_minima) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
             
    cursor.execute(sql, (
        produto.nome, produto.descricao, produto.categoria, 
        produto.unidade_medida, produto.quantidade_estoque, produto.quantidade_minima
    ))
    
    # Commit e encerramento
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201


# ROTA PARA BUSCAR PRODUTOS COM FILTROS OPCIONAIS
@app.route('/api/produtos', methods=['GET'])
def buscar_produtos():
    # Captura filtros via parâmetros da URL
    nome = request.args.get('nome')
    categoria = request.args.get('categoria')

    # Abre a conexão solicitando retornos tabulares em dicionário
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "SELECT * FROM produto WHERE 1=1"
    params = []

    # Aplicação dinâmica de filtros
    if nome:
        sql += " AND nome LIKE %s"
        params.append(f"%{nome}%")

    if categoria:
        sql += " AND categoria = %s"
        params.append(categoria)

    # Execução e coleta dos resultados
    cursor.execute(sql, tuple(params))
    produtos = cursor.fetchall()
    
    # Fechamento de conexão
    cursor.close()
    conn.close()

    return jsonify(produtos), 200


# ROTA PARA EDITAR/ATUALIZAR UM PRODUTO
@app.route('/api/produtos/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    # Lê os dados em JSON recebidos
    dados = request.get_json()
    
    # Instancia objeto Produto
    produto = Produto(
        dados['nome'], dados['descricao'], dados['categoria'], 
        dados['unidade_medida'], dados['quantidade_estoque'], dados['quantidade_minima']
    )
    
    # Abre conexão
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query de atualização SQL
    sql = """UPDATE produto SET 
                nome = %s, descricao = %s, categoria = %s, 
                unidade_medida = %s, quantidade_estoque = %s, quantidade_minima = %s 
             WHERE id_produto = %s"""
             
    # Injeta os valores na instrução SQL
    cursor.execute(sql, (
        produto.nome, produto.descricao, produto.categoria, 
        produto.unidade_medida, produto.quantidade_estoque, produto.quantidade_minima, id_produto
    ))
    
    # Persiste alterações e encerra o fluxo
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto atualizado com sucesso!"}), 200


# ROTA PARA EXCLUIR UM PRODUTO
@app.route('/api/produtos/<int:id_produto>', methods=['DELETE'])
def excluir_produto(id_produto):
    # Abre a conexão
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Executa a remoção com o identificador 'id_produto'
    cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
    
    # Confirma e fecha
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Produto excluído com sucesso!"}), 200


# ==========================================
# 4. ROTAS DE CONSULTA
# ==========================================

# ROTA PARA AGENDAR NOVA CONSULTA
@app.route('/api/consulta', methods=['POST'])
def cadastrar_consulta():
    # Obtém o JSON contendo as chaves estrangeiras 'id_cliente' e 'id_profissional'
    dados = request.get_json()
    
    # Conecta ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL de inserção incluindo as Chaves Estrangeiras (FK)
    sql = """INSERT INTO consulta (id_cliente, id_profissional, data_consulta, horario, status, observacoes) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
             
    # Utiliza dados.get() nos campos opcionais 'status' e 'observacoes' para prevenir erros de KeyError
    cursor.execute(sql, (
        dados['id_cliente'], dados['id_profissional'], 
        dados['data_consulta'], dados['horario'], 
        dados.get('status', 'Agendada'), dados.get('observacoes')
    ))
    
    # Salva e fecha a conexão
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Consulta agendada com sucesso!"}), 201


# ROTA PARA BUSCAR CONSULTAS (COM INNER JOIN)
@app.route('/api/consulta', methods=['GET'])
def buscar_consultas():
    # Abre a conexão solicitando o retorno como dicionários Python
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Consulta avançada com JOIN para buscar o NOME do cliente e o NOME do profissional no mesmo resultado
    sql = """
        SELECT c.id_consulta, c.data_consulta, c.horario, c.status, c.observacoes,
               cli.nome AS nome_cliente, prof.nome AS nome_profissional
        FROM consulta c
        JOIN cliente cli ON c.id_cliente = cli.id_cliente
        JOIN profissional prof ON c.id_profissional = prof.id_profissional
    """

    # Executa a query sem filtros adicionais
    cursor.execute(sql)
    consultas = cursor.fetchall()
    
    # Encerra conexão
    cursor.close()
    conn.close()

    return jsonify(consultas), 200


# ROTA PARA ATUALIZAR UMA CONSULTA
@app.route('/api/consulta/<int:id_consulta>', methods=['PUT'])
def atualizar_consulta(id_consulta):
    # Captura dados JSON de atualização
    dados = request.get_json()
    
    # Instancia objeto da Model Consulta
    consulta = Consulta(
        dados['id_cliente'], dados['id_profissional'], 
        dados['data_consulta'], dados['horario'], 
        dados['status'], dados['observacoes']
    )
    
    # Conecta ao MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SQL com 7 marcações de posição (%s)
    sql = """UPDATE consulta SET 
                id_cliente = %s, 
                id_profissional = %s, 
                data_consulta = %s, 
                horario = %s, 
                status = %s, 
                observacoes = %s 
             WHERE id_consulta = %s"""
             
    # Envia rigorosamente os 7 valores ordenados no cursor.execute
    cursor.execute(sql, (
        consulta.id_cliente, 
        consulta.id_profissional, 
        consulta.data_consulta, 
        consulta.horario, 
        consulta.status, 
        consulta.observacoes, 
        id_consulta  
    ))

    # Persiste os novos dados e encerra a sessão do banco
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Consulta atualizada com sucesso!"}), 200


# ROTA PARA CANCELAR/EXCLUIR UMA CONSULTA
@app.route('/api/consulta/<int:id_consulta>', methods=['DELETE'])
def excluir_consulta(id_consulta):
    # Conecta ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Executa o comando SQL para deletar a consulta pelo seu ID
    cursor.execute("DELETE FROM consulta WHERE id_consulta = %s", (id_consulta,))
    
    # Persiste e fecha o banco
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Consulta excluída com sucesso!"}), 200


# ==========================================
# 5. ROTAS DE MOVIMENTAÇÃO DE ESTOQUE
# ==========================================

# ROTA PARA REGISTRAR ENTRADA/SAÍDA DE ESTOQUE (REGRA DE NEGÓCIO DUPLA)
@app.route('/api/movimentacao', methods=['POST'])
def registrar_movimentacao():
    # Coleta as informações de movimentação
    dados = request.get_json()
    
    id_produto = dados['id_produto']
    tipo = dados['tipo'] # 'Entrada' ou 'Saída'
    quantidade = dados['quantidade']
    
    # Conecta ao banco
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # REGRA 1: Grava o registro histórico da movimentação com data/hora automática NOW()
    sql_mov = """INSERT INTO movimentacao_estoque (id_produto, tipo, quantidade, data_movimentacao, motivo) 
                 VALUES (%s, %s, %s, NOW(), %s)"""
    cursor.execute(sql_mov, (id_produto, tipo, quantidade, dados.get('motivo')))
    
    # REGRA 2: Atualiza o saldo do produto na tabela 'produto' dependendo do tipo da transação
    if tipo == 'Entrada':
        sql_prod = "UPDATE produto SET quantidade_estoque = quantidade_estoque + %s WHERE id_produto = %s"
    else: # Tipo igual a 'Saída'
        sql_prod = "UPDATE produto SET quantidade_estoque = quantidade_estoque - %s WHERE id_produto = %s"
        
    cursor.execute(sql_prod, (quantidade, id_produto))
    
    # Confirma ambas as transações de forma atômica
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": f"Movimentação de {tipo} registrada e estoque atualizado!"}), 201


# ROTA PARA HISTÓRICO DE MOVIMENTAÇÕES (BUSCA COM JOIN FIXO)
@app.route('/api/movimentacao', methods=['GET'])
def buscar_movimentacoes():
    # Captura parâmetros opcionais na query string
    nome = request.args.get('nome')
    tipo = request.args.get('tipo')
    
    # Conecta no MySQL configurado com retorno em dicionários
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # SQL base contendo o JOIN com a tabela de produtos para trazer o nome do item
    sql = """
        SELECT m.id_movimentacao, m.tipo, m.quantidade, m.data_movimentacao, m.motivo, 
               p.nome AS nome_produto
        FROM movimentacao_estoque m
        JOIN produto p ON m.id_produto = p.id_produto
        WHERE 1=1
    """
    params = []

    # Aplicação dinâmica de filtros
    if nome:
        sql += " AND p.nome LIKE %s"
        params.append(f"%{nome}%")

    if tipo:
        sql += " AND m.tipo = %s"
        params.append(tipo)

    # Executa e converte os dados
    cursor.execute(sql, tuple(params))
    movimentacoes = cursor.fetchall()
    
    # Encerra o uso da conexão
    cursor.close()  
    conn.close()

    return jsonify(movimentacoes), 200

# OBSERVAÇÃO TÉCNICA: As rotas DELETE e PUT foram omitidas intencionalmente 
# da classe Movimentacao_estoque para preservação da integridade auditável do histórico de estoque.


# ==========================================
# 6. ROTAS DE FEEDBACK
# ==========================================

# ROTA PARA REGISTRAR UM NOVO FEEDBACK
@app.route('/api/feedback', methods=['POST'])
def cadastrar_feedback():
    # Obtém o JSON enviado pelo cliente com id_consulta, nota e comentário
    dados = request.get_json()
    
    # Abre a conexão
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insere o registro utilizando a função nativa do MySQL CURDATE() para gravar a data atual
    sql = """INSERT INTO feedback (id_consulta, nota, comentario, data_feedback) 
             VALUES (%s, %s, %s, CURDATE())"""
             
    cursor.execute(sql, (
        dados['id_consulta'], 
        dados['nota'], 
        dados.get('comentario')
    ))
    
    # Grava e finaliza
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Feedback enviado com sucesso!"}), 201


# ROTA PARA CONSULTAR FEEDBACKS REGISTRADOS
@app.route('/api/feedback', methods=['GET'])
def buscar_feedbacks():
    # Filtro opcional por ID da consulta
    id_consulta = request.args.get('id_consulta')
    
    # Abre conexão
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Traz informações do feedback combinadas com os dados básicos da consulta associada
    sql = """
        SELECT f.id_feedback, f.nota, f.comentario, f.data_feedback, 
               c.id_consulta, c.data_consulta, c.horario
        FROM feedback f
        JOIN consulta c ON f.id_consulta = c.id_consulta
        WHERE 1=1
    """
    params = []

    if id_consulta:
        sql += " AND c.id_consulta = %s"
        params.append(id_consulta)

    # Execução da query
    cursor.execute(sql, tuple(params))
    feedbacks = cursor.fetchall()
    
    # Encerramento dos recursos
    cursor.close()  
    conn.close()

    return jsonify(feedbacks), 200


# ROTA PARA ATUALIZAR UM FEEDBACK EXISTENTE
@app.route('/api/feedback/<int:id_feedback>', methods=['PUT'])
def atualizar_feedback(id_feedback):
    # Coleta a requisição JSON
    dados = request.get_json()
    
    # Instancia o objeto Feedback
    feedback = Feedback(
        dados['id_consulta'], 
        dados['nota'], 
        dados.get('comentario')
    )
    
    # Conecta no MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query de atualização SQL
    sql = """UPDATE feedback SET 
                id_consulta = %s, 
                nota = %s, 
                comentario = %s 
             WHERE id_feedback = %s"""
             
    cursor.execute(sql, (
        feedback.id_consulta, 
        feedback.nota, 
        feedback.comentario, 
        id_feedback  
    ))

    # Grava a alteração e encerra
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Feedback atualizado com sucesso!"}), 200


# ROTA PARA EXCLUIR UM FEEDBACK
@app.route('/api/feedback/<int:id_feedback>', methods=['DELETE'])
def excluir_feedback(id_feedback):
    # Conecta no banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Inicia e executa a instrução DELETE no feedback especificado
    cursor.execute("DELETE FROM feedback WHERE id_feedback = %s", (id_feedback,))
    
    # Confirma alteração e finaliza a conexão
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Feedback excluído com sucesso!"}), 200


# ==========================================
# INICIALIZAÇÃO DA APLICAÇÃO FLASK
# ==========================================
if __name__ == '__main__':
    # Roda o servidor web em modo debug facilitando visualizar logs e alterações em tempo real
    app.run(debug=True)
