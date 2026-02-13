import pandas as pd
from src.database.database import DB
from dotenv import load_dotenv
import os






LINK = 'https://www.instagram.com/p/DRszG9Skb21/'









load_dotenv()
TABLE_P = os.getenv('TABLE_P')
TABLE_W_S = os.getenv('TABLE_W_S')
TABLE_C = os.getenv('TABLE_C')
DIM_P = os.getenv('DIM_P')
DIM_C = os.getenv('DIM_C')
T_FATO = os.getenv('T_FATO')



query = f'''
-- dim post


--  tb_fato

insert {T_FATO}(dim_post_id_post,dim_sentimento_id_sentimentos,dim_comentario_id_comentario,dim_calendario_id_data)
select 
	 p.id_posts,
	 case 
		when upper(cs.sentimento) = 'POSITIVO' then 1
		when upper(cs.sentimento) = 'NEGATIVO' then 0
		when upper(cs.sentimento) = 'NEUTRO' then 3
        else 4
	 END id_sentimento,
	 c.id_comentarios,
	 p.data_post
from {TABLE_P} p
inner join {TABLE_C} c on p.id_posts = c.posts_id_posts
inner join {TABLE_W_S} cs on cs.comentarios_id_comentarios  = c.id_comentarios
where p.link = '{LINK}'


'''

query_dim_post = f'''
    insert into {DIM_P}(id_post,post)
        select 
            p.id_posts,
            p.link 
        from {TABLE_P} p 
        where p.link = '{LINK}';
'''

query_dim_comentarios = f'''
    insert into {DIM_C}(id_comentario,comentario)
        select 
            c.id_comentarios,
            c.comentario 
        from {TABLE_P} p 
        inner join {TABLE_C} c on p.id_posts = c.Posts_id_posts
        where p.link = '{LINK}';
'''



#DELETAR INFORMAÇÕES PARA SEREM INSERIDAS NOVAMENTE

query_delete_C = f'''
delete c from {DIM_C} c
inner join {T_FATO} ft on ft.dim_comentario_id_comentario = c.id_comentario
inner join {DIM_P} p on p.id_post = ft.dim_post_id_post
where p.post = '{LINK}' ;
'''

query_delete_p = f'''
delete p  from {DIM_P} p 
where p.post = '{LINK}';

'''



DB.execute_query(query_delete_C)
DB.execute_query(query_delete_p)
DB.execute_query(query_dim_post)
DB.execute_query(query_dim_comentarios)
DB.execute_query(query)



