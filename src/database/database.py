import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import pandas as pd
import os


load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE =  os.getenv('DATABASE')
TABLE_P = os.getenv('TABLE_P')
TABLE_C = os.getenv('TABLE_C')
TABLE_W_S = os.getenv('TABLE_W_S')

class DB:
    def __init__(self):
        pass

    @staticmethod
    def conexao():
        con = mysql.connector.connect(
                                    host=HOST, 
                                    user=USER, 
                                    password=PASSWORD, 
                                    database=DATABASE)
        
        con.set_charset_collation(charset='utf8mb4',collation='utf8mb4_unicode_ci')

        return con
    


    @classmethod
    def insert_post(cls, data, nome_pagina, link ):
        '''
        Método para persistir dados de Post
        '''
        con = DB.conexao()
        cursor = con.cursor()
        
        query = f'insert into {TABLE_P} (link, data_post,nome_pagina) values("{link}","{data}","{nome_pagina}")'

        cursor.execute(query)
        con.commit()
            
        ultimo_id =  cursor.lastrowid    
        
       
        return ultimo_id
    
    @classmethod
    def insert_comment(cls, list_comment:list , id_post ):
        '''
        Método para persistir comentários coletados do Instagram.
        '''
        con = DB.conexao()
        cursor = con.cursor()
        
        df = pd.DataFrame(list_comment,columns=['comentarios'])
        
        for comment in df['comentarios']:
    
            query = f'insert into {TABLE_C}(comentario,Posts_id_posts) values ("{comment}","{id_post}")'
            
            cursor.execute(query)
            
            con.commit()




    @classmethod
    def insert_comment_w_sentiment(cls,sentiment,comentario_id,post_id):
        con = DB.conexao()
        cursor = con.cursor()
        #df = pd.DataFrame(list_comment,columns=['comentarios'])
    
    
        query = f'insert into {TABLE_W_S} (sentimento,comentarios_id_comentarios,Posts_id_posts) values("{sentiment}", "{comentario_id}","{post_id}")'    
        cursor.execute(query)
        con.commit()
        
        
        
          
        con.close()
     


    @classmethod
    def read_table(cls,query):
        con = DB.conexao()
        cursor = con.cursor()
        comentarios = list()
        cursor.execute(query)
        
        for i in cursor:
            comentarios.append(i)
        
        return comentarios
    












