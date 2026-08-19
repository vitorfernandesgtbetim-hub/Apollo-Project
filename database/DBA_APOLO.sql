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
    status ENUM('Ativo','Inativo') DEFAULT 'Ativo',
    senha VARCHAR(100) NOT NULL
);

INSERT INTO profissional
(nome, cpf, telefone, email, cargo, especialidade, status, senha)
VALUE
('Ana Carolina Mendes', '12345678901', '(31) 98811-2233', 'ana.mendes@clinica.com', 'Dentista', 'Clínica Geral', 'Ativo', SHA2('Clinica@123', 256)),
('Bruno Henrique Alves', '23456789012', '(31) 97722-3344', 'bruno.alves@clinica.com', 'Dentista', 'Ortodontia', 'Ativo', SHA2('Clinica@123', 256)),
('Camila Fernanda Souza', '34567890123', '(31) 96633-4455', 'camila.souza@clinica.com', 'Dentista', 'Endodontia', 'Ativo', SHA2('Clinica@123', 256)),
('Daniel Oliveira Costa', '45678901234', '(31) 95544-5566', 'daniel.costa@clinica.com', 'Dentista', 'Implantodontia', 'Ativo', SHA2('Clinica@123', 256)),
('Eduarda Martins Lima', '56789012345', '(31) 94455-6677', 'eduarda.lima@clinica.com', 'Dentista', 'Odontopediatria', 'Ativo', SHA2('Clinica@123', 256)),
('Felipe Augusto Rocha', '67890123456', '(31) 93366-7788', 'felipe.rocha@clinica.com', 'Dentista', 'Periodontia', 'Ativo', SHA2('Clinica@123', 256)),
('Gabriela Ribeiro Santos', '78901234567', '(31) 92277-8899', 'gabriela.santos@clinica.com', 'Dentista', 'Clínica Geral', 'Ativo', SHA2('Clinica@123', 256)),
('Henrique Souza Melo', '89012345678', '(31) 91188-9900', 'henrique.melo@clinica.com', 'Dentista', 'Prótese Dentária', 'Ativo', SHA2('Clinica@123', 256)),
('Isabela Cristina Alves', '90123456789', '(31) 90099-1122', 'isabela.alves@clinica.com', 'Dentista', 'Ortodontia', 'Ativo', SHA2('Clinica@123', 256)),
('João Pedro Ferreira', '01234567890', '(31) 98910-2233', 'joao.ferreira@clinica.com', 'Auxiliar', NULL, 'Ativo', SHA2('Clinica@123', 256)),
('Larissa Gomes Pereira', '11223344556', '(31) 97821-3344', 'larissa.pereira@clinica.com', 'Recepcionista', NULL, 'Ativo', SHA2('Clinica@123', 256)),
('Marcos Vinicius Silva', '22334455667', '(31) 96732-4455', 'marcos.silva@clinica.com', 'Auxiliar', NULL, 'Ativo', SHA2('Clinica@123', 256)),
('Natalia Freitas Castro', '33445566778', '(31) 95643-5566', 'natalia.castro@clinica.com', 'Recepcionista', NULL, 'Ativo', SHA2('Clinica@123', 256)),
('Otavio Ribeiro Lima', '44556677889', '(31) 94554-6677', 'otavio.lima@clinica.com', 'Dentista', 'Cirurgia Bucomaxilofacial', 'Ativo', SHA2('Clinica@123', 256)),
('Patricia Almeida Souza', '55667788990', '(31) 93465-7788', 'patricia.souza@clinica.com', 'Dentista', 'Harmonização Orofacial', 'Ativo', SHA2('Clinica@123', 256)),
('Rafael Martins Dias', '66778899001', '(31) 92376-8899', 'rafael.dias@clinica.com', 'Dentista', 'Clínica Geral', 'Ativo', SHA2('Clinica@123', 256)),
('Sabrina Moreira Lopes', '77889900112', '(31) 91287-9900', 'sabrina.lopes@clinica.com', 'Auxiliar', NULL, 'Ativo', SHA2('Clinica@123', 256)),
('Thiago Barbosa Mendes', '88990011223', '(31) 90198-1122', 'thiago.mendes@clinica.com', 'Dentista', 'Implantodontia', 'Inativo', SHA2('Clinica@123', 256));

# TABELA CLIENTES
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_nascimento TIMESTAMP,
    cep VARCHAR(9),
    rua VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(60),
    cidade VARCHAR(60),
    estado CHAR(2),
    data_cadastro DATE,
    status ENUM('Ativo','Inativo') DEFAULT 'Ativo',
    senha VARCHAR(255) NOT NULL
);

INSERT INTO cliente
(nome, cpf, telefone, email, data_nascimento, cep, rua, numero, bairro, cidade, estado, data_cadastro, status, senha)
VALUES
('Lucas Gabriel Souza', '10123456789', '(31) 98810-1001', 'lucas.souza@email.com', '1998-04-12', '32600-100', 'Rua das Flores', '120', 'Centro', 'Betim', 'MG', '2025-01-10', 'Ativo', SHA2('Clinica@123', 256)),
('Mariana Alves Costa', '10234567890', '(31) 97720-1002', 'mariana.costa@email.com', '1995-08-23', '32610-200', 'Rua Ipê Amarelo', '245', 'Jardim Alterosas', 'Betim', 'MG', '2025-01-15', 'Ativo', SHA2('Clinica@123', 256)),
('Pedro Henrique Lima', '10345678901', '(31) 96630-1003', 'pedro.lima@email.com', '2001-02-17', '32620-300', 'Avenida Amazonas', '850', 'Brasiléia', 'Betim', 'MG', '2025-02-03', 'Ativo', SHA2('Clinica@123', 256)),
('Julia Martins Rocha', '10456789012', '(31) 95540-1004', 'julia.rocha@email.com', '1999-11-05', '32630-400', 'Rua Bela Vista', '78', 'Ingá', 'Betim', 'MG', '2025-02-08', 'Ativo', SHA2('Clinica@123', 256)),
('Gabriel Oliveira Santos', '10567890123', '(31) 94450-1005', 'gabriel.santos@email.com', '1997-06-19', '32640-500', 'Rua São Paulo', '312', 'Petrovale', 'Betim', 'MG', '2025-02-15', 'Ativo', SHA2('Clinica@123', 256)),
('Beatriz Fernanda Alves', '10678901234', '(31) 93360-1006', 'beatriz.alves@email.com', '2003-03-28', '32650-600', 'Rua Minas Gerais', '145', 'Centro', 'Betim', 'MG', '2025-02-21', 'Ativo', SHA2('Clinica@123', 256)),
('Rafael Augusto Mendes', '10789012345', '(31) 92270-1007', 'rafael.mendes@email.com', '1992-09-14', '32660-700', 'Rua dos Ipês', '500', 'Citrolândia', 'Betim', 'MG', '2025-03-02', 'Ativo', SHA2('Clinica@123', 256)),
('Larissa Cristina Souza', '10890123456', '(31) 91180-1008', 'larissa.souza@email.com', '1996-12-30', '32670-800', 'Rua Primavera', '90', 'PTB', 'Betim', 'MG', '2025-03-10', 'Ativo', SHA2('Clinica@123', 256)),
('Matheus Vinicius Pereira', '10901234567', '(31) 90090-1009', 'matheus.pereira@email.com', '2000-01-21', '32680-900', 'Rua Ouro Preto', '415', 'Niterói', 'Betim', 'MG', '2025-03-14', 'Ativo', SHA2('Clinica@123', 256)),
('Amanda Ribeiro Lima', '11012345678', '(31) 98900-1010', 'amanda.lima@email.com', '1994-07-08', '32690-010', 'Rua Tiradentes', '200', 'Centro', 'Betim', 'MG', '2025-03-19', 'Ativo', SHA2('Clinica@123', 256)),
('Joao Victor Alves', '11123456789', '(31) 97800-1011', 'joao.alves@email.com', '1998-10-25', '32600-110', 'Rua Bahia', '321', 'Angola', 'Betim', 'MG', '2025-03-25', 'Ativo', SHA2('Clinica@123', 256)),
('Camila Rodrigues Silva', '11234567890', '(31) 96700-1012', 'camila.silva@email.com', '2002-05-16', '32610-210', 'Rua Ceará', '145', 'Jardim Teresópolis', 'Betim', 'MG', '2025-04-01', 'Ativo', SHA2('Clinica@123', 256)),
('Felipe Eduardo Castro', '11345678901', '(31) 95600-1013', 'felipe.castro@email.com', '1990-03-09', '32620-310', 'Rua Goiás', '87', 'Centro', 'Betim', 'MG', '2025-04-06', 'Ativo', SHA2('Clinica@123', 256)),
('Isabela Martins Souza', '11456789012', '(31) 94500-1014', 'isabela.souza@email.com', '2004-09-12', '32630-410', 'Rua Paraná', '234', 'Ingá', 'Betim', 'MG', '2025-04-12', 'Ativo', SHA2('Clinica@123', 256)),
('Gustavo Henrique Lima', '11567890123', '(31) 93400-1015', 'gustavo.lima@email.com', '1993-01-27', '32640-510', 'Rua Rio de Janeiro', '610', 'Brasiléia', 'Betim', 'MG', '2025-04-20', 'Ativo', SHA2('Clinica@123', 256)),
('Sofia Almeida Rocha', '11678901234', '(31) 92300-1016', 'sofia.rocha@email.com', '2001-06-04', '32650-610', 'Rua Espírito Santo', '155', 'Centro', 'Betim', 'MG', '2025-05-03', 'Ativo', SHA2('Clinica@123', 256)),
('Daniel Henrique Souza', '11789012345', '(31) 91200-1017', 'daniel.souza@email.com', '1989-12-18', '32660-710', 'Rua Pará', '345', 'Citrolândia', 'Betim', 'MG', '2025-05-11', 'Ativo', SHA2('Clinica@123', 256)),
('Clara Beatriz Mendes', '11890123456', '(31) 90100-1018', 'clara.mendes@email.com', '1997-02-11', '32670-810', 'Rua Amazonas', '76', 'PTB', 'Betim', 'MG', '2025-05-16', 'Ativo', SHA2('Clinica@123', 256)),
('Vinicius Gabriel Alves', '11901234567', '(31) 99010-1019', 'vinicius.alves@email.com', '1995-11-29', '32680-910', 'Rua Sergipe', '520', 'Niterói', 'Betim', 'MG', '2025-05-22', 'Ativo', SHA2('Clinica@123', 256)),
('Helena Martins Costa', '12012345678', '(31) 98110-1020', 'helena.costa@email.com', '1999-04-03', '32690-020', 'Rua Bahia', '88', 'Centro', 'Betim', 'MG', '2025-06-01', 'Ativo', SHA2('Clinica@123', 256)),
('Arthur Gabriel Lima', '12123456789', '(31) 97210-1021', 'arthur.lima@email.com', '2002-08-15', '32600-120', 'Rua das Acácias', '132', 'Angola', 'Betim', 'MG', '2025-06-08', 'Ativo', SHA2('Clinica@123', 256)),
('Manuela Cristina Souza', '12234567890', '(31) 96310-1022', 'manuela.souza@email.com', '1996-05-22', '32610-220', 'Rua das Palmeiras', '290', 'Alterosas', 'Betim', 'MG', '2025-06-15', 'Ativo', SHA2('Clinica@123', 256)),
('Enzo Miguel Santos', '12345678902', '(31) 95410-1023', 'enzo.santos@email.com', '2010-10-10', '32620-320', 'Rua Diamantina', '45', 'Centro', 'Betim', 'MG', '2025-06-20', 'Ativo', SHA2('Clinica@123', 256)),
('Valentina Ribeiro Alves', '12456789013', '(31) 94510-1024', 'valentina.alves@email.com', '2005-07-17', '32630-420', 'Rua Ouro Branco', '178', 'Ingá', 'Betim', 'MG', '2025-06-25', 'Ativo', SHA2('Clinica@123', 256)),
('Miguel Angelo Pereira', '12567890124', '(31) 93610-1025', 'miguel.pereira@email.com', '1991-03-26', '32640-520', 'Rua Contagem', '390', 'Brasiléia', 'Betim', 'MG', '2025-07-02', 'Ativo', SHA2('Clinica@123', 256)),
('Alice Fernanda Lima', '12678901235', '(31) 92710-1026', 'alice.lima@email.com', '1998-09-30', '32650-620', 'Rua Sabará', '120', 'Centro', 'Betim', 'MG', '2025-07-09', 'Ativo', SHA2('Clinica@123', 256)),
('Theo Martins Silva', '12789012346', '(31) 91810-1027', 'theo.silva@email.com', '2003-12-07', '32660-720', 'Rua Betim', '205', 'Citrolândia', 'Betim', 'MG', '2025-07-15', 'Ativo', SHA2('Clinica@123', 256)),
('Laura Cristina Rocha', '12890123457', '(31) 90910-1028', 'laura.rocha@email.com', '1994-06-13', '32670-820', 'Rua Itatiaia', '75', 'PTB', 'Betim', 'MG', '2025-07-20', 'Ativo', SHA2('Clinica@123', 256)),
('Bernardo Souza Costa', '12901234568', '(31) 99020-1029', 'bernardo.costa@email.com', '1987-01-31', '32680-920', 'Rua Nova Lima', '450', 'Niterói', 'Betim', 'MG', '2025-07-27', 'Ativo', SHA2('Clinica@123', 256)),
('Livia Gabriela Alves', '13012345679', '(31) 98120-1030', 'livia.alves@email.com', '2000-11-20', '32690-030', 'Rua Mariana', '180', 'Centro', 'Betim', 'MG', '2025-08-02', 'Inativo', SHA2('Clinica@123', 256));

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

INSERT INTO produto
(nome, descricao, categoria, unidade_medida, quantidade_estoque, quantidade_minima)
VALUES
('Luva de Procedimento P', 'Luva descartável para procedimentos odontológicos', 'EPI', 'Caixa', 42, 10),
('Luva de Procedimento M', 'Luva descartável para procedimentos odontológicos', 'EPI', 'Caixa', 58, 10),
('Luva de Procedimento G', 'Luva descartável para procedimentos odontológicos', 'EPI', 'Caixa', 35, 10),
('Máscara Cirúrgica', 'Máscara descartável tripla camada', 'EPI', 'Caixa', 25, 8),
('Touca Descartável', 'Touca descartável para procedimentos', 'EPI', 'Pacote', 18, 5),
('Avental Descartável', 'Avental descartável hospitalar', 'EPI', 'Unidade', 75, 20),
('Seringa 5ml', 'Seringa descartável de 5ml', 'Materiais', 'Caixa', 30, 8),
('Agulha Gengival Curta', 'Agulha odontológica curta', 'Materiais', 'Caixa', 22, 5),
('Agulha Gengival Longa', 'Agulha odontológica longa', 'Materiais', 'Caixa', 17, 5),
('Anestésico Lidocaína', 'Tubetes de anestésico odontológico', 'Anestésicos', 'Caixa', 14, 4),
('Anestésico Mepivacaína', 'Tubetes de anestésico odontológico', 'Anestésicos', 'Caixa', 11, 4),
('Resina Fotopolimerizável A1', 'Resina composta odontológica', 'Dentística', 'Seringa', 16, 5),
('Resina Fotopolimerizável A2', 'Resina composta odontológica', 'Dentística', 'Seringa', 19, 5),
('Resina Fotopolimerizável A3', 'Resina composta odontológica', 'Dentística', 'Seringa', 12, 5),
('Ácido Fosfórico 37%', 'Ácido para condicionamento dental', 'Dentística', 'Seringa', 20, 5),
('Adesivo Dental', 'Sistema adesivo odontológico', 'Dentística', 'Frasco', 13, 4),
('Flúor Gel', 'Gel fluoretado para aplicação odontológica', 'Prevenção', 'Frasco', 24, 6),
('Algodão em Rolo', 'Algodão odontológico em rolos', 'Materiais', 'Pacote', 40, 10),
('Gaze Estéril', 'Gaze estéril para procedimentos', 'Materiais', 'Pacote', 32, 8),
('Fio Dental', 'Fio dental para orientação ao paciente', 'Higiene', 'Unidade', 65, 15),
('Escova Dental', 'Escova dental para pacientes', 'Higiene', 'Unidade', 48, 10),
('Pasta Profilática', 'Pasta para profilaxia dental', 'Prevenção', 'Tubo', 15, 5),
('Cimento Odontológico', 'Cimento odontológico temporário', 'Materiais', 'Frasco', 9, 3),
('Fio Retrator Gengival', 'Fio para retração gengival', 'Periodontia', 'Caixa', 8, 3),
('Broca Carbide', 'Broca odontológica carbide', 'Instrumentais', 'Unidade', 27, 8),
('Broca Diamantada', 'Broca odontológica diamantada', 'Instrumentais', 'Unidade', 35, 10),
('Copo Descartável', 'Copo descartável para atendimento', 'Descartáveis', 'Pacote', 45, 10),
('Sugador Descartável', 'Sugadores descartáveis odontológicos', 'Descartáveis', 'Pacote', 38, 10),
('Papel Toalha', 'Papel toalha para higiene', 'Higiene', 'Pacote', 21, 5),
('Álcool 70%', 'Álcool para higienização de superfícies', 'Higiene', 'Frasco', 18, 5);

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

INSERT INTO consulta
(id_cliente, id_profissional, data_consulta, horario, status, observacoes)
VALUES
(1, 1, '2026-01-05', '08:00:00', 'Concluída', 'Avaliação odontológica inicial'),
(2, 2, '2026-01-05', '09:00:00', 'Concluída', 'Avaliação ortodôntica'),
(3, 3, '2026-01-06', '10:00:00', 'Concluída', 'Avaliação de dor dentária'),
(4, 4, '2026-01-06', '14:00:00', 'Concluída', 'Avaliação para implante'),
(5, 5, '2026-01-07', '15:00:00', 'Concluída', 'Avaliação odontopediátrica'),
(6, 1, '2026-01-08', '08:30:00', 'Concluída', 'Limpeza dental'),
(7, 6, '2026-01-09', '09:30:00', 'Concluída', 'Avaliação periodontal'),
(8, 7, '2026-01-10', '10:30:00', 'Concluída', 'Consulta de rotina'),
(9, 8, '2026-01-12', '13:30:00', 'Concluída', 'Avaliação para prótese'),
(10, 9, '2026-01-13', '14:30:00', 'Concluída', 'Manutenção ortodôntica'),
(11, 2, '2026-01-14', '15:30:00', 'Cancelada', 'Paciente solicitou cancelamento'),
(12, 3, '2026-01-15', '08:00:00', 'Concluída', 'Tratamento endodôntico'),
(13, 4, '2026-01-16', '09:00:00', 'Concluída', 'Avaliação de implante'),
(14, 5, '2026-01-17', '10:00:00', 'Concluída', 'Consulta preventiva'),
(15, 6, '2026-01-19', '14:00:00', 'Concluída', 'Tratamento periodontal'),
(16, 7, '2026-01-20', '15:00:00', 'Concluída', 'Consulta de rotina'),
(17, 8, '2026-01-21', '16:00:00', 'Concluída', 'Avaliação protética'),
(18, 9, '2026-01-22', '08:30:00', 'Concluída', 'Avaliação ortodôntica'),
(19, 14, '2026-01-23', '09:30:00', 'Concluída', 'Avaliação cirúrgica'),
(20, 15, '2026-01-24', '10:30:00', 'Concluída', 'Avaliação estética'),
(1, 1, '2026-02-02', '08:00:00', 'Concluída', 'Retorno para acompanhamento'),
(2, 2, '2026-02-03', '09:00:00', 'Concluída', 'Acompanhamento ortodôntico'),
(3, 3, '2026-02-04', '10:00:00', 'Concluída', 'Continuação do tratamento'),
(4, 4, '2026-02-05', '14:00:00', 'Concluída', 'Planejamento de implante'),
(5, 5, '2026-02-06', '15:00:00', 'Concluída', 'Acompanhamento infantil'),
(6, 1, '2026-02-07', '08:30:00', 'Concluída', 'Nova profilaxia'),
(7, 6, '2026-02-09', '09:30:00', 'Cancelada', 'Paciente não compareceu'),
(8, 7, '2026-02-10', '10:30:00', 'Concluída', 'Avaliação preventiva'),
(9, 8, '2026-02-11', '13:30:00', 'Concluída', 'Ajuste de prótese'),
(10, 9, '2026-02-12', '14:30:00', 'Concluída', 'Manutenção ortodôntica'),
(11, 2, '2026-02-13', '15:30:00', 'Agendada', 'Retorno ortodôntico'),
(12, 3, '2026-02-14', '08:00:00', 'Agendada', 'Continuação do tratamento'),
(13, 4, '2026-02-16', '09:00:00', 'Agendada', 'Procedimento de implante'),
(14, 5, '2026-02-17', '10:00:00', 'Agendada', 'Avaliação preventiva'),
(15, 6, '2026-02-18', '14:00:00', 'Agendada', 'Acompanhamento periodontal'),
(16, 7, '2026-02-19', '15:00:00', 'Agendada', 'Consulta de rotina'),
(17, 8, '2026-02-20', '16:00:00', 'Agendada', 'Ajuste protético'),
(18, 9, '2026-02-21', '08:30:00', 'Agendada', 'Manutenção ortodôntica'),
(19, 14, '2026-02-23', '09:30:00', 'Agendada', 'Avaliação cirúrgica'),
(20, 15, '2026-02-24', '10:30:00', 'Agendada', 'Procedimento estético');

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

INSERT INTO movimentacao_estoque
(id_produto, tipo, quantidade, data_movimentacao, motivo)
VALUES
(1, 'Entrada', 50, '2026-01-02 08:30:00', 'Compra de materiais'),
(2, 'Entrada', 70, '2026-01-02 08:35:00', 'Compra de materiais'),
(3, 'Entrada', 40, '2026-01-02 08:40:00', 'Compra de materiais'),
(4, 'Entrada', 30, '2026-01-03 09:00:00', 'Reposição de estoque'),
(5, 'Entrada', 20, '2026-01-03 09:10:00', 'Reposição de estoque'),
(6, 'Entrada', 100, '2026-01-03 09:20:00', 'Compra de materiais'),
(7, 'Entrada', 40, '2026-01-04 10:00:00', 'Compra de seringas'),
(8, 'Entrada', 25, '2026-01-04 10:15:00', 'Compra de agulhas'),
(9, 'Entrada', 20, '2026-01-04 10:20:00', 'Compra de agulhas'),
(10, 'Entrada', 20, '2026-01-05 11:00:00', 'Compra de anestésicos'),
(11, 'Entrada', 15, '2026-01-05 11:15:00', 'Compra de anestésicos'),
(12, 'Entrada', 20, '2026-01-06 08:00:00', 'Compra de resinas'),
(13, 'Entrada', 25, '2026-01-06 08:15:00', 'Compra de resinas'),
(14, 'Entrada', 15, '2026-01-06 08:30:00', 'Compra de resinas'),
(15, 'Entrada', 25, '2026-01-07 09:00:00', 'Reposição de material'),
(16, 'Entrada', 15, '2026-01-07 09:15:00', 'Compra de adesivos'),
(17, 'Entrada', 30, '2026-01-08 10:00:00', 'Compra de flúor'),
(18, 'Entrada', 50, '2026-01-08 10:15:00', 'Compra de algodão'),
(19, 'Entrada', 40, '2026-01-08 10:30:00', 'Compra de gaze'),
(1, 'Saída', 8, '2026-01-10 17:00:00', 'Utilização em procedimentos'),
(2, 'Saída', 12, '2026-01-10 17:05:00', 'Utilização em procedimentos'),
(4, 'Saída', 5, '2026-01-11 16:00:00', 'Utilização em atendimentos'),
(7, 'Saída', 10, '2026-01-12 17:00:00', 'Utilização em consultas'),
(8, 'Saída', 4, '2026-01-12 17:10:00', 'Utilização em consultas'),
(10, 'Saída', 5, '2026-01-13 17:30:00', 'Procedimentos anestésicos'),
(12, 'Saída', 4, '2026-01-14 18:00:00', 'Restaurações'),
(13, 'Saída', 5, '2026-01-15 18:00:00', 'Restaurações'),
(17, 'Saída', 6, '2026-01-16 17:00:00', 'Aplicações de flúor'),
(18, 'Saída', 10, '2026-01-17 16:30:00', 'Procedimentos'),
(19, 'Saída', 8, '2026-01-17 16:45:00', 'Procedimentos'),
(20, 'Saída', 15, '2026-01-18 17:00:00', 'Entrega aos pacientes'),
(21, 'Saída', 12, '2026-01-19 17:00:00', 'Entrega aos pacientes'),
(25, 'Saída', 7, '2026-01-20 18:00:00', 'Procedimentos'),
(26, 'Saída', 10, '2026-01-21 18:00:00', 'Procedimentos'),
(27, 'Saída', 12, '2026-01-22 17:30:00', 'Atendimentos'),
(28, 'Saída', 10, '2026-01-23 17:30:00', 'Atendimentos'),
(29, 'Saída', 8, '2026-01-24 17:30:00', 'Higienização'),
(30, 'Saída', 5, '2026-01-25 17:30:00', 'Higienização'),
(1, 'Entrada', 30, '2026-02-01 08:00:00', 'Reposição de estoque'),
(2, 'Entrada', 40, '2026-02-01 08:15:00', 'Reposição de estoque'),
(10, 'Entrada', 10, '2026-02-02 09:00:00', 'Reposição de anestésicos'),
(12, 'Entrada', 15, '2026-02-03 09:30:00', 'Reposição de resina'),
(17, 'Entrada', 20, '2026-02-04 10:00:00', 'Reposição de flúor'),
(18, 'Entrada', 30, '2026-02-05 10:30:00', 'Reposição de algodão'),
(19, 'Entrada', 25, '2026-02-06 11:00:00', 'Reposição de gaze'),
(4, 'Saída', 7, '2026-02-07 17:00:00', 'Atendimentos odontológicos'),
(7, 'Saída', 8, '2026-02-08 17:30:00', 'Atendimentos odontológicos'),
(10, 'Saída', 3, '2026-02-09 18:00:00', 'Procedimentos'),
(12, 'Saída', 5, '2026-02-10 18:00:00', 'Restaurações'),
(13, 'Saída', 4, '2026-02-11 18:00:00', 'Restaurações'),
(17, 'Saída', 5, '2026-02-12 17:30:00', 'Prevenção'),
(18, 'Saída', 7, '2026-02-13 17:30:00', 'Procedimentos'),
(19, 'Saída', 6, '2026-02-14 17:30:00', 'Procedimentos');

# TABELA FEEDBACK
CREATE TABLE feedback (
    id_feedback INT AUTO_INCREMENT PRIMARY KEY,
    id_consulta INT NOT NULL,
    nota INT NOT NULL,
    comentario TEXT,
    data_feedback DATE,
    
    FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);


INSERT INTO feedback
(id_consulta, nota, comentario, data_feedback)
VALUES
(1, 5, 'Excelente atendimento e equipe muito atenciosa.', '2026-01-05'),
(2, 5, 'Profissional explicou todo o tratamento com clareza.', '2026-01-05'),
(3, 4, 'Fui bem atendido e o procedimento foi tranquilo.', '2026-01-06'),
(4, 5, 'Ótimo atendimento, fiquei muito satisfeito.', '2026-01-06'),
(5, 5, 'Atendimento excelente e muito cuidadoso.', '2026-01-07'),
(6, 4, 'Gostei bastante da limpeza e do atendimento.', '2026-01-08'),
(7, 5, 'Profissional muito atencioso e cuidadoso.', '2026-01-09'),
(8, 5, 'Ambiente organizado e atendimento excelente.', '2026-01-10'),
(9, 4, 'Gostei do atendimento e das explicações.', '2026-01-12'),
(10, 5, 'Muito bom, sempre sou bem atendido.', '2026-01-13'),
(12, 5, 'O tratamento foi explicado de forma muito clara.', '2026-01-15'),
(13, 4, 'Atendimento muito bom.', '2026-01-16'),
(14, 5, 'Excelente atendimento para meu filho.', '2026-01-17'),
(15, 5, 'Profissional excelente e muito cuidadoso.', '2026-01-19'),
(16, 4, 'Consulta rápida e atendimento muito bom.', '2026-01-20'),
(17, 5, 'Fiquei muito satisfeito com o resultado.', '2026-01-21'),
(18, 5, 'Excelente profissional.', '2026-01-22'),
(19, 4, 'Fui muito bem orientado durante a consulta.', '2026-01-23'),
(20, 5, 'Atendimento excelente e ambiente agradável.', '2026-01-24'),
(21, 5, 'Ótimo acompanhamento.', '2026-02-02'),
(22, 4, 'Profissional muito atencioso.', '2026-02-03'),
(23, 5, 'Estou gostando bastante do tratamento.', '2026-02-04'),
(24, 5, 'Excelente planejamento do procedimento.', '2026-02-05'),
(25, 4, 'Muito bom atendimento.', '2026-02-06'),
(26, 5, 'Gostei muito da nova profilaxia.', '2026-02-07'),
(28, 5, 'Atendimento rápido e eficiente.', '2026-02-10'),
(29, 4, 'Fiquei satisfeito com o resultado.', '2026-02-11'),
(30, 5, 'Excelente manutenção.', '2026-02-12');
