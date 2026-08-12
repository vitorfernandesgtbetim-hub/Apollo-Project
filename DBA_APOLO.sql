CREATE DATABASE DBA_APOLO;

# TABELA PROFISSIONAL 
CREATE TABLE profissional (
    id_profissional INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    cargo VARCHAR(50) NOT NULL,
    especialidade VARCHAR(100),
    status ENUM('Ativo','Inativo') DEFAULT 'Ativo'
);

# TABELA CLIENTES
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_nascimento DATE,
    cep VARCHAR(9),
    rua VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(60),
    cidade VARCHAR(60),
    estado CHAR(2),
    data_cadastro DATE,
    status ENUM('Ativo','Inativo') DEFAULT 'Ativo'
);

# TABELA PRODUTO
CREATE TABLE produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    categoria VARCHAR(50),
    unidade_medida VARCHAR(20),
    quantidade_estoque INT DEFAULT 0,
    quantidade_minima INT DEFAULT 0
);

#TABELA CONSULTA
CREATE TABLE consulta (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_profissional INT NOT NULL,
    data_consulta DATE NOT NULL,
    horario TIME NOT NULL,
    status ENUM('Agendada','Concluída','Cancelada') DEFAULT 'Agendada',
    observacoes TEXT,

    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_profissional) REFERENCES profissional(id_profissional)
);

# TABELA MOVIMENTAÇÃO DE ESTOQUE
CREATE TABLE movimentacao_estoque (
    id_movimentacao INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    tipo ENUM('Entrada','Saída') NOT NULL,
    quantidade INT NOT NULL,
    data_movimentacao DATETIME NOT NULL,
    motivo VARCHAR(100),

    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

# TABELA FEEDBACK
CREATE TABLE feedback (
    id_feedback INT AUTO_INCREMENT PRIMARY KEY,
    id_consulta INT NOT NULL,
    nota INT NOT NULL,
    comentario TEXT,
    data_feedback DATE,

    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);