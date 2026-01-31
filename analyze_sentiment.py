from database.database import DB
from classes.process.pnl import Pnl
from classes.process.analyze_sentiment import Analyzer
from classes.Instagram.scrapy import Scrape
from llmms.teste import Chat
import pandas as pd
from dotenv import load_dotenv
import os



con = DB.conexao()
load_dotenv()

df = Pnl.get_comment(con)


#comentarios = Pnl.apply_stop_word(df)
#comentarios = 


comentarios = DB.read_table(os.getenv('TABLE_W_S'))

for comentario in comentarios:
    #sentimento = Analyzer.analyze_sentiment(comentario)
    sentimento = Chat.classificator(comment=comentario[1])
    DB.insert_comment_w_sentiment(comentario[1],sentimento)


 
