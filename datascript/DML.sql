/*Inserção de elementos na base de dados*/

ALTER SEQUENCE endereco_ENDERECO_ID_seq RESTART WITH 1;
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Tiradentes','Morumbi','São Paulo','São Paulo','08260-310');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Paulista','Bom Clima','São Paulo','São Paulo','08420-220');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Brasil','Tatuapé','São Paulo','São Paulo','08485-501');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Tupinamba','Penha','São Paulo','São Paulo','04736-050');

ALTER SEQUENCE DIETA_ID RESTART WITH 1;
insert into DIETA(comida, frequencia, restricoes) values ('Arroz com frango', '2 vezes ao dia', 'Nao tem restricao');
insert into DIETA(comida, frequencia, restricoes) values ('Racao sabor carne', '3 vezes ao dia', 'Nao tem restricao');
insert into DIETA(comida, frequencia, restricoes) values ('Legumes cozidos com frango', '2 vezes ao dia', 'Não tem restricao');
insert into DIETA(comida, frequencia, restricoes) values ('Racao sabor frango', '3 vezes ao dia', 'Não tem restricao');

ALTER SEQUENCE REL_ID RESTART WITH 1;
ALTER SEQUENCE medicamento_ped_REL_ID_seq RESTART WITH 1;
 insert into medicamento(animal_id, med_id) values (1, 1);
 insert into medicamento(animal_id, med_id) values (2, 2);
 insert into medicamento(animal_id, med_id) values (3, 3);
 insert into medicamento(animal_id, med_id) values (4, 4);
 
ALTER SEQUENCE dono_DONO_ID_seq RESTART WITH 1;
 insert into dono(cpf_cliente, telefone, endereco_id, nome_cli, sobrenome_cli, contato_emergencia, data_nascimento) values ('699.275.270-71','(68) 99642-5211', 1, 'Rafaela Ayla', 'Brito', '(69) 92798-6020', '04/01/1945');
 insert into dono(cpf_cliente, telefone, endereco_id, nome_cli, sobrenome_cli, contato_emergencia, data_nascimento) values ('508.114.225-50','(98) 98954-0908', 2, 'Filipe Fernando', 'Rezende', '(98) 93857-1713', '01/01/1999');
 insert into dono(cpf_cliente, telefone, endereco_id, nome_cli, sobrenome_cli, contato_emergencia, data_nascimento) values ('460.888.232-59','(91) 99728-5957', 3, 'Maria', 'Oliveira', '(98) 93857-1713', '01/01/1999');
 insert into dono(cpf_cliente, telefone, endereco_id, nome_cli, sobrenome_cli, contato_emergencia, data_nascimento) values ('812.839.851-28','((62) 98948-6097', 4, 'Juca', 'Bortoloti', '(98) 93857-1713', '01/01/1999');

 ALTER SEQUENCE animal_ANIMAL_ID_seq RESTART WITH 1;
 insert into animal(dono_id, dieta_id, nome, data_nascimento, condicao_especial) values (1, 4, 'Bob', '20/02/2010', 'alergia a perfume');
 insert into animal(dono_id, dieta_id, nome, data_nascimento, condicao_especial) values (2, 3, 'Fifi', '03/12/2004', 'asma');
 insert into animal(dono_id, dieta_id, nome, data_nascimento, condicao_especial) values (3, 2, 'Mel', '16/03/2011', 'nenhuma');
 insert into animal(dono_id, dieta_id, nome, data_nascimento, condicao_especial) values (4, 1, 'Totó', '01/7/2008', 'sensibilidade nos olhos');

 ALTER SEQUENCE medicacao_MED_ID_seq RESTART WITH 1;
 insert into medicacao(registro_federal, nome, fabricante, circunstancia) values ('31023660', 'Vermífugo Bayer Drontal Plus Sabor Carne', 'Drontal, Bayer', 'Tratamento de verminoses no intestino');
 insert into medicacao(registro_federal, nome, fabricante, circunstancia) values ('3104948-1', 'Antipulgas e Carrapatos MSD Bravecto para Cães de 10 a 20 Kg', 'Bravecto, MSD Saúde Animal', 'Antipulga');
 insert into medicacao(registro_federal, nome, fabricante, circunstancia) values ('3103532', 'Complexo Vitamínico Aminomix Pet', 'Vetnil', 'Melhoria das estruturas orgânicas');
 insert into medicacao(registro_federal, nome, fabricante, circunstancia) values ('10007230000609', 'Colírio Lacri 15ml Agener União para Cães', 'Agener União', 'Cuidados diários');
