/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     01/12/2021 22:59:58                          */
/*==============================================================*/


/*==============================================================*/
/* Table: EDERECO                                               */
/*==============================================================*/

create table ENDERECO (
   ENDERECO_ID          SERIAL                 not null,
   RUA                  VARCHAR(50)          not null,
   COMPLEMENTO          VARCHAR(50)          null,
   BAIRRO               VARCHAR(50)          not null,
   CIDADE               VARCHAR(50)          not null,
   ESTADO               VARCHAR(50)          not null,
   CEP                  VARCHAR(50)           not null,
   constraint PK_ENDERECO primary key (ENDERECO_ID)
);

create table DONO (
   DONO_ID           SERIAL               not null,
   CPF_CLIENTE          VARCHAR(50)          not null,
   TELEFONE              VARCHAR(50)          not null,
   ENDERECO_ID          INTEGER              not null,
   NOME_CLI             VARCHAR(50)          null,
   SOBRENOME_CLI        VARCHAR(50)          null,
   CONTATO_EMERGENCIA      varchar(50)          not null,
   DATA_NASCIMENTO      varchar(50)          not null,
   constraint PK_DONO primary key (DONO_ID),
   constraint FK_DONO_R13_ENDERECO foreign key (ENDERECO_ID)
      references ENDERECO (ENDERECO_ID)
      on delete restrict on update restrict
);

create table ANIMAL(
    ANIMAL_ID SERIAL not null,
    DONO_ID INTEGER not null,
    DIETA_ID INTEGER not null,
    NOME varchar(50) not null,
    DATA_NASCIMENTO varchar(50) not null,
    CONDICAO_ESPECIAL varchar(100) not null,
    constraint PK_ANIMAL primary key (ANIMAL_ID),
     constraint FK_ANIMAL_R13_DONO foreign key (DONO_ID)
      references DONO (DONO_ID)
      on delete restrict on update restrict,
      constraint FK_ANIMAL_R13_DIETA foreign key (DIETA_ID)
      references DIETA (DIETA_ID)
      on delete restrict on update restrict
);

create table MEDICACAO(
    MED_ID SERIAL not null,
    REGISTRO_FEDERAL varchar(50) not null ,
    NOME varchar(50) not null,
    FABRICANTE varchar(50) not null,
    CIRCUNSTANCIA varchar(100) not null,
    constraint PK_MEDICACO primary key (MED_ID)
);

create table DIETA(
        DIETA_ID SERIAL       not null,
        COMIDA      varchar(50)  not null,
        FREQUENCIA  varchar(50)  not null,
        RESTIRCOES  varchar(100) not null,
        constraint PK_ALIMENTACAO primary key (DIETA_ID)
);

create table MEDICAMENTO_PET(
        REL_ID  SERIAL  not null,
        ANIMAL_ID INTEGER  not null,
        MED_ID  INTEGER not null,
        constraint PK_ALIMENTACAO primary key (REL_ID),
        constraint FK_MEDICAMENTO_R13_ANIMAL foreign key (ANIMAL_ID)
      references ANIMAL (ANIMAL_ID)
      on delete restrict on update restrict,
      constraint FK_ANIMAL_R13_MEDICAMENTO foreign key (MED_ID)
      references MEDICACAO (MED_ID)
      on delete restrict on update restrict
);
