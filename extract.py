import os
import json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup 
import ast
from src.classes.Instagram.login import Login
from src.classes.Instagram.scrapy import Scrape
from src.classes.Instagram.post_instagram import PostInstagram
from src.classes.process.pnl import Pnl
from src.classes.visualization.plot_word_cloud import Plot_word_cloud
from src.classes.visualization.plot_bar import Plot_bar
from src.classes.process.analyze_sentiment  import Analyzer
from src.database.database import DB
from src.database.normalization_comments import Normalization_comments
from mysql.connector import Error
import mysql.connector
from pathlib import Path
from tqdm import tqdm
import time

ROOT_PATH = Path(__file__).parent

'''
- Gov.Br - Isenção do Imposto de Renda (@govbr) - 30/11/2025: https://www.instagram.com/p/DRszG9Skb21/

- Caso do Cão Orelha (@folhadespaulo) - 12/02/2026: https://www.instagram.com/p/DUqQiuhDJB4/ 

- Realização show de Lady Gaga (@betour_rj) - 04/05/2025: https://www.instagram.com/p/DJOA1XbM4gZ/

- Criação de vídeo com IA (@geracaodeimagem) - 28/12/2025: https://www.instagram.com/p/DS0xxvuERoQ/

'''



#novo método 
LINK = 'https://www.instagram.com/p/DUqQiuhDJB4/'  
DATA = '2026/02/12'
NOME_PAGINA = 'Folha de S.Paulo'



#dados do posto do instagram
input_Instagram = PostInstagram(LINK, DATA,NOME_PAGINA)

start_time = time.time()
#login instagram
login = Login.inicializarNavegador(input_Instagram.set_link())

#scrollando página
Scrape.scroll_comments(login)

#capturando html e salvando html
site_html = Scrape.Scraping(login)

comentarios = Scrape.get_comments(site_html)
end_time = time.time()
tempo_de_coleta = end_time - start_time
#imprimindo dados do post do instagram
print('Dados do posto do instagram: \n')
print('______________________________\n')
print('Link do Post: ', input_Instagram.set_link(),'\n')
print('Data do Post:', input_Instagram.set_data(),'\n')
print('Fonte:', input_Instagram.set_nome_pagina(),'\n')
print('Tempo de coleta: ', round(tempo_de_coleta/60,0),' minutos \n')
print('______________________________\n')
print('Comentarios coletados abaixo: ')
cont = 0
for comentario in tqdm(comentarios,desc='Coletando comentarios'):
    time.sleep(0.001)
    cont += 1
comentarios_normalizados = Normalization_comments.normalization_comment(comentarios)


print('Número do comentários coletados: ',cont)

print('Inserindo dados no banco de dados')

try:
    id_post = DB.insert_post(
                    input_Instagram.set_data(),
                    input_Instagram.set_nome_pagina(),
                    input_Instagram.set_link()
    )

    DB.insert_comment(comentarios_normalizados,id_post)

except mysql.connector.IntegrityError  as e:
    print(f'Erro apresentado: {e}')


