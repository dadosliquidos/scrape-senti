import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pathlib import Path
import pandas as pd
import emoji
import re
import unicodedata

#leitura dos arquivo com os comentários
ROOT_PATH = Path(__file__).parent.parent.parent



def remover_acentos_vogais(texto):
    # Decompõe os caracteres (ex: 'ã' vira 'a' + '~')
    processado = unicodedata.normalize('NFD', texto)
    resultado = []
    
    # Definimos as vogais base para conferência
    vogais = "aeiouAEIOU"
    
    for i, char in enumerate(processado):
        # Se for uma marca de acento (Combining Mark)
        if unicodedata.combining(char):
            # Verificamos se o caractere anterior era uma vogal
            if i > 0 and processado[i-1] in vogais:
                continue # Pula o acento (remove)
        
        resultado.append(char)
        
    # Reagrupa e volta para o formato padrão (NFC)
    return unicodedata.normalize('NFC', "".join(resultado))


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
        stopwords_pt.append('ta')
        stopwords_pt.append('vai')
        stopwords_pt.append('já')
        stopwords_pt.append('aí')
        stopwords_pt.append('ai')
        stopwords_pt.append('q')
        stopwords_pt.append('deu')
        stopwords_pt.append('ja')
        stopwords_pt.append('aí')
        stopwords_pt.append('não')
        stopwords_pt.append('nao')

        lista_tokens = []
        comentarios = []

        for comentario in dataframe['comentario']:
            somente_letras = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚãõÃÕçÇ\s]','',comentario.lower())
            somente_letras = remover_acentos_vogais(somente_letras)
            tokens = word_tokenize(somente_letras)
            tokens_wo_stopwords = [t.upper() for t in tokens if t not in stopwords_pt]
            
            comentarios.append(' '.join(tokens_wo_stopwords)) #lista de comentarios
           
        return comentarios
    
    @classmethod
    def only_emojis(cls,dataframe):
        '''
            r retona comentarios somente com emoijs
            
        '''
        
        

       
        comentarios = []

        for comentario in dataframe['comentario']:
            somente_emojis = [c for c in comentario if emoji.is_emoji(c)]
            
            
            
            comentarios.append(' '.join(somente_emojis)) #lista de comentarios
           
        return comentarios