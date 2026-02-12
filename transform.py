from src.database.database import DB
from src.classes.process.pnl import Pnl
from src.classes.process.analyze_sentiment import Analyzer
from src.classes.Instagram.scrapy import Scrape
from src.LLM.classificator import Chat
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm
import os
import time



load_dotenv()
TABLE_C = os.getenv('TABLE_C') 
TABLE_P = os.getenv('TABLE_P')
LINK = 'https://www.instagram.com/p/DUBjtCAEfVI/'

query = f'''
 
select  
	p.id_posts,
    c.id_comentarios,
    c.comentario
from {TABLE_P} p 
inner join {TABLE_C} c on p.id_posts = c.posts_id_posts
where link = '{LINK}'
'''

comentarios = DB.read_table(query)

for index in tqdm(comentarios,desc='Extraindo análise de sentimentos'): 
    time.sleep(0.001)
    sentimento = Chat.classificator(comment=index[2])
    DB.insert_comment_w_sentiment(
                sentiment=sentimento,
                comentario_id=index[1],
                post_id=index[0])
