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
   BAIRRO               VARCHAR(50)          not null,
   CIDADE               VARCHAR(50)          not null,
   ESTADO               VARCHAR(50)          not null,
   CEP                  VARCHAR(50)           not null,
   constraint PK_ENDERECO primary key (ENDERECO_ID)
);

/* O ESTILO É ESSE */