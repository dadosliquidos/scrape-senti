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


#cursor = con.cursor()
 

#cursor.execute('select * from comentarios')


#for (id, comentario,sentimento) in cursor:
#    print(id,comentario,sentimento)

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
    def insert_comment(cls, list_comment,data,fonte_jornal ):
        con = DB.conexao()
        cursor = con.cursor()
        df = pd.DataFrame(list_comment,columns=['comentarios'])
    
        for comment in df['comentarios']:
    
            query = 'insert into comentarios (comentario,data_post,fonte_jornal) values("{}", "{}" , "{}")'.format(comment,data,fonte_jornal)
            
            cursor.execute(query)
            con.commit()
            
        
        
        print('Comentários persistidos com sucesso.')
        con.close()



    @classmethod
    def insert_comment_w_sentiment(cls, comment, sentiment):
        con = DB.conexao()
        cursor = con.cursor()
        #df = pd.DataFrame(list_comment,columns=['comentarios'])
    
    
        query = 'insert into comentarios_w_sentiment (comentario,sentimento) values("{}", "{}")'.format(comment,sentiment)
        print(query)    
        cursor.execute(query)
        con.commit()
        
        
        print('Comentários persistidos com sucesso.')      
        con.close()



     








