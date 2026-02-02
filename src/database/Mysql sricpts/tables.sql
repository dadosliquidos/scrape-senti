
CREATE TABLE IF NOT EXISTS tb_Posts (
  id_posts INT NOT NULL primary key auto_increment,
  link TEXT NULL unique,
  data_post DATE NULL,
  nome_pagina VARCHAR(60) NULL
  );


CREATE TABLE IF NOT EXISTS tb_comentarios (
  id_comentarios INT NOT NULL primary key auto_increment,
  comentario TEXT NULL,
  Posts_id_posts INT NOT NULL,
  CONSTRAINT fk_comentarios_Posts
    FOREIGN KEY (Posts_id_posts)
    REFERENCES tb_Posts (id_posts)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
    
    

CREATE TABLE IF NOT EXISTS tb_comentarios_com_sentimentos (
   id_c_sentimentos INT NOT NULL primary key auto_increment,
  sentimento VARCHAR(45) NULL,
  comentarios_id_comentarios INT NOT NULL,
  Posts_id_posts INT NOT NULL,
  CONSTRAINT fk_comentarios_com_sentimentos_comentarios
    FOREIGN KEY (comentarios_id_comentarios)
    REFERENCES  tb_comentarios (id_comentarios)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_comentarios_com_sentimentos_Posts
    FOREIGN KEY (Posts_id_posts)
    REFERENCES tb_Posts (id_posts)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


