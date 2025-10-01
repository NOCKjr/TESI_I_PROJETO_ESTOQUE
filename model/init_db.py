import sqlite3
import os
import constants

def create_db():

    db_dir = os.path.dirname(constants.DB_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    if not os.path.exists(constants.DB_PATH):
        con = sqlite3.connect(constants.DB_PATH)
        cur = con.cursor() 
        cur.executescript('''
            CREATE TABLE endereco(
                end_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                end_logradouro varchar(50) NOT NULL,
                end_numero INTEGER NOT NULL,
                end_bairro VARCHAR(50) NOT NULL,
                end_cidade VARCHAR(50) NOT NULL,
                end_estado VARCHAR(50) NOT NULL,
                end_cep VARCHAR(10) NOT NULL,
                end_complemento VARCHAR(100) NULL,
                end_ponto_referencia VARCHAR(100) NULL);
                    
            CREATE TABLE escola(
                esc_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                esc_nome VARCHAR(64) NOT NULL,
                esc_numero_alunos INT(8) NOT NULL,
                esc_end_id INTEGER NOT NULL,
                FOREIGN KEY (esc_end_id) REFERENCES endereco(end_id));
                    
            CREATE TABLE fornecedor(
                for_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                for_razao_social VARCHAR(128) NOT NULL,
                for_contato VARCHAR(128) NOT NULL);
                    
            CREATE TABLE insumo(
                ins_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                ins_nome VARCHAR(64) NOT NULL,
                ins_media_consumida INTEGER NOT_NULL,
                ins_quantidade_estoque INTEGER NOT NULL,
                ins_med_id INTEGER,
                FOREIGN KEY (ins_med_id) REFERENCES medida(med_id));
                    
            CREATE TABLE item(
                itm_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                itm_quantidade INTEGER NOT NULL,
                fk_itm_ins_id INTEGER NOT NULL,
                fk_itm_mov_id INTEGER NOT NULL,
                FOREIGN KEY (fk_itm_ins_id) REFERENCES insumo(ins_id),
                FOREIGN KEY (fk_itm_mov_id) REFERENCES movimentacao(mov_id));
                    
            CREATE TABLE medida(
                med_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                med_unidade VARCHAR(32) NOT NULL);
                    
            CREATE TABLE movimentacao(
                mov_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                mov_data DATE NOT NULL,
                mov_tipo VARCHAR(1) NOT NULL,
                fk_mov_usu_id INTEGER,
                fk_mov_for_id INTEGER,
                fk_mov_esc_id INTEGER,
                FOREIGN KEY (fk_mov_usu_id) REFERENCES usuario(usu_id),
                FOREIGN KEY (fk_mov_for_id) REFERENCES fornecedor(for_id),
                FOREIGN KEY (fk_mov_esc_id) REFERENCES escola(esc_id)
                );
                    
            CREATE TABLE usuario(
                usu_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usu_nick VARCHAR(64) NOT NULL,
                usu_email VARCHAR(100) NOT NULL,
                usu_senha VARCHAR(64) NOT NULL,
                usu_tipo CHAR(1) NOT NULL);
        ''')
        con.commit()
        con.close()