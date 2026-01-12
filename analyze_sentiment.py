from database.database import DB
from classes.process.pnl import Pnl
from classes.process.analyze_sentiment import Analyzer
import pandas as pd

con = DB.conexao()


df = Pnl.get_comment(con)


comentarios = Pnl.apply_stop_word(df)




for comentario in comentarios:
    sentimento = Analyzer.analyze_sentiment(comentario)
    DB.insert_comment_w_sentiment(comentario,sentimento)
    