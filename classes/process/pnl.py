import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pathlib import Path
import pandas as pd
import re


#leitura dos arquivo com os comentários
ROOT_PATH = Path(__file__).parent.parent.parent

class Pnl:
    def __init__(self):
        pass


    @classmethod
    def get_comment(cls,con):
        '''
            Retorna DataFrame dos comentários obtidos 
        '''
       
        ''' col_name = ['Comentários']
        dataframe = pd.read_csv(ROOT_PATH / 'database' / nome_arquivo, sep=';', encoding='utf-8',names=['comentarios'], engine='python',on_bad_lines='skip')'''
        dataframe = pd.read_sql_query('select * from comentarios',con)

        return dataframe
    
    @classmethod
    def apply_stop_word(cls,dataframe):
        '''
            r retona comentarios sem os stop word
            
        '''
        
        
        stopwords_pt = stopwords.words('portuguese') # dicionario que contem os stop word pt-br
        stopwords_pt.append('pra')
        stopwords_pt.append('tá')
        stopwords_pt.append('vai')
        stopwords_pt.append('já')
        stopwords_pt.append('aí')

        lista_tokens = []
        comentarios = []

        for comentario in dataframe['comentario']:
            somente_letras = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚãõÃÕçÇ]',' ',comentario.lower())
            tokens = word_tokenize(somente_letras)
            tokens_wo_stopwords = [t for t in tokens if t not in stopwords_pt]
            
            comentarios.append(' '.join(tokens_wo_stopwords)) #lista de comentarios
           
        return comentarios
