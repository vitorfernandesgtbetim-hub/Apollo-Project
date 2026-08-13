class Profissional:
    def __init__(self, id_profissional, nome, cpf, telefone, email, cargp, especialidade, status):
        self.id_profissional = id_profissional
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.cargp = cargp
        self.especialidade = especialidade
        self.status = status


class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, email, data_nascimento, cep, rua, numero, bairro, cidade, estado, data_cadastro, status, observacoes):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.data_cadastro = data_cadastro
        self.status = status
        self.observacoes = observacoes


class Produto:
    def __init__(self, id_produto, nome, descricao, categoria, unidade_medida, quantidade_estoque, quantidad_minima):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.unidade_medida = unidade_medida
        self.quantidade_estoque = quantidade_estoque
        self.quantidad_minima = quantidad_minima


class Consulta:
    def __init__(self, id_consulta, id_cliente, id_profissional, data_consulta, horario, status, observacoes):
        self.id_consulta = id_consulta
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.data_consulta = data_consulta
        self.horario = horario
        self.status = status
        self.observacoes = observacoes


class Movimentacao_estoque:
    def __init__(self, id_movimentacao, id_produto, tipo, quantidade, data_movimentacao, motivo):
        self.id_movimentacao = id_movimentacao
        self.id_produto = id_produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.data_movimentacao = data_movimentacao
        self.motivo = motivo


class Feedback:
    def __init__(self, id_feedback, id_consulta, nota, comentario, data_feedback):
        self.id_feedback = id_feedback
        self.id_consulta = id_consulta
        self.nota = nota
        self.comentario = comentario
        self.data_feedback = data_feedback
