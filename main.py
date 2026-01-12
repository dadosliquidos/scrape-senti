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
from classes.Instagram.login import Login
from classes.Instagram.scrapy import Scrape
from classes.Instagram.post_instagram import PostInstagram
from classes.process.pnl import Pnl
from classes.visualization.plot_word_cloud import Plot_word_cloud
from classes.visualization.plot_bar import Plot_bar
from classes.process.analyze_sentiment  import Analyzer
from database.database import DB
from database.normalization_comments import Normalization_comments
from pathlib import Path

ROOT_PATH = Path(__file__).parent
#login
'''login = Login.inicializarNavegador('https://www.instagram.com/p/DRK6RxfkXDV')
# html da pagina

#scrollando página
Scrape.scroll_comments(login)

#capturando html e salvando html
site_html = Scrape.Scraping(login)

comentarios = Scrape.get_comments(site_html)

for comentario in comentarios:
    print(comentario)


'''

#novo método 
LINK = 'https://www.instagram.com/doldiarioonline/p/DGDmjvbRGtu/' 
DATA = '2025/02/12'
FONTE_JORNAL = 'Diário online do Pará'



#dados do posto do instagram
input_Instagram = PostInstagram(LINK, DATA,FONTE_JORNAL)

#login instagram
login = Login.inicializarNavegador(input_Instagram.set_link())

#scrollando página
Scrape.scroll_comments(login)

#capturando html e salvando html
site_html = Scrape.Scraping(login)

comentarios = Scrape.get_comments(site_html)

#imprimindo dados do post do instagram
print('Dados do posto do instagram: \n')
print('______________________________\n')
print('Link do Post: ', input_Instagram.set_link(),'\n')
print('Data do Post:', input_Instagram.set_data(),'\n')
print('Fonte:', input_Instagram.set_fonte_jornal(),'\n')
print('______________________________\n')
print('Comentarios coletados abaixo: ')
cont = 0
for comentario in comentarios:
    cont += 1
comentarios_normalizados = Normalization_comments.normalization_comment(comentarios)


print('Número do comentários coletados: ',cont)

print('Inserindo no banco de dados')
DB.insert_comment(
                    comentarios_normalizados,
                    input_Instagram.set_data(),
                    input_Instagram.set_fonte_jornal()
                  )













'''
time.sleep(2)
Scrape.scroll_comments(login)

time.sleep(2)
siteHtml = login.page_source
print('html capturado.')



ob_html = BeautifulSoup(siteHtml,'html.parser')

print('html coletado com sucessso.')

login.quit()

comentarios = ob_html.find_all('div','html-div xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x9f619 xjbqb8w x78zum5 x15mokao x1ga7v0g x16uus16 xbiv7yw x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1')
time.sleep(2)

contador = 0

for comentario in comentarios:
    print(comentario.text.strip())
    contador += 1

print('Comentários coletados: ', contador)'''





#Scrape.interact_element(login)










#Scrape.scroll_comments(login)


#login.implicitly_wait(10)

#html_content = Scrape.scroll_comments(login)

#print(html_content)






































#html_page = Scrape.Scraping(login)


#print(html_page)



#list_comments = Scrape.get_comments(html_page)
#print(list_comments)
'''num_comment = 0
for comment in list_comments:
   num_comment += 1
   print(comment)
   print('teste')'''

#print(num_comment)
'''
with open(ROOT_PATH / 'database' / 'comentarios.csv', 'w',encoding='utf-8') as arquivo:
      
      for comment in list_comments:
         arquivo.write(comment+'\n')'''
#with open('teste','w') as file:
 #   file.write('Isso aqui é um teste.')

#df = Pnl.get_comment('comentarios.csv')
#Plot_bar.plot(df)
#Plot_word_cloud.plot(Pnl.apply_stop_word(df))

#Plot_word_cloud.plot(Pnl.apply_stop_word(df))


#time.sleep(3)

#Plot_bar.plot(df)

#df = pd.DataFrame(list_comments,columns=['comentarios'])
#print(df)



#DB.insert_comment(list_comments)

