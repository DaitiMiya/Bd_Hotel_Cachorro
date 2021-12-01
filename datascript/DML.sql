/*Inserção de elementos na base de dados*/

ALTER SEQUENCE endereco_ENDERECO_ID_seq RESTART WITH 1;
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Tiradentes','Morumbi','São Paulo','São Paulo','08260-310');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Paulista','Bom Clima','São Paulo','São Paulo','08420-220');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Brasil','Tatuapé','São Paulo','São Paulo','08485-501');
insert into endereco(rua, bairro, cidade, estado, cep) values ('Avenida Tupinamba','Penha','São Paulo','São Paulo','04736-050');
