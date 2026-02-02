import matplotlib.pyplot as plt
import pandas as pd
from src.classes.process.analyze_sentiment import Analyzer
from pathlib import Path
import matplotlib
matplotlib.use('Agg') # or 'SVG'



ROOT_PATH = Path(__file__).parent.parent.parent


class Plot_bar:
    def __init__(self):
        pass

    
    @classmethod
    def plot(cls, dataframe):

    

        #analyze_sentiment = Analyzer.analyze_sentiment
        dataframe['sentimento'] = dataframe['comentarios'].apply(Analyzer.analyze_sentiment)
        dataframe['count'] = 1
        dataframe['comentarios'] = dataframe['comentarios'].dropna()

        
        
        dataframe = dataframe.groupby('sentimento').count().reset_index()


        plt.bar(dataframe['sentimento'],dataframe['count'], color='#00FA9A')
        plt.ylabel('QTDE DE COMENTÁRIOS')
        plt.title('Análise de sentimentos')

        for i, value in enumerate(dataframe['count']):
            plt.text(i, value + 2, str(value), ha='center')
        plt.savefig(ROOT_PATH / 'app' / 'static' / 'imagem' / 'bar.png')
        plt.close()




       


