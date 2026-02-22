drop schema Data_warehouse;
create schema Data_warehouse;
use Data_warehouse;
SET FOREIGN_KEY_CHECKS=1;





CREATE TABLE IF NOT EXISTS dim_post (
  id_post INT NOT NULL  PRIMARY KEY,
  post TEXT NULL);



CREATE TABLE IF NOT EXISTS dim_sentimento (
  id_sentimentos INT NOT NULL primary key,
  sentimento VARCHAR(45) );



CREATE TABLE IF NOT EXISTS dim_comentario (
  id_comentario INT NOT NULL primary KEY,
  comentario TEXT NULL);




CREATE TABLE IF NOT EXISTS dim_calendario (
  id_data DATE NOT NULL primary key,
	mes	 VARCHAR(45) NULL,
   ano VARCHAR(45) NULL);
   
   



CREATE TABLE IF NOT EXISTS Tb_fatos_analise_comentario (
  dim_post_id_post INT NOT NULL,
  dim_sentimento_id_sentimentos INT NOT NULL,
  dim_comentario_id_comentario INT NOT NULL,
  dim_calendario_id_data DATE NOT NULL,
 

  CONSTRAINT fk_Tb_fatos_análise_comentário_dim_post
    FOREIGN KEY (dim_post_id_post)
    REFERENCES dim_post (id_post),
  
  CONSTRAINT fk_Tb_fatos_análise_comentário_dim_sentimento
    FOREIGN KEY (dim_sentimento_id_sentimentos)
    REFERENCES dim_sentimento (id_sentimentos),
 
 CONSTRAINT fk_Tb_fatos_análise_comentário_dim_comentario
    FOREIGN KEY (dim_comentario_id_comentario)
    REFERENCES dim_comentario (id_comentario)
    ON DELETE CASCADE,
  
  CONSTRAINT fk_Tb_fatos_análise_comentário_dim_calendario
    FOREIGN KEY (dim_calendario_id_data)
    REFERENCES dim_calendario (id_data)
)



