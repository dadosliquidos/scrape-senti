from ollama import chat
from ollama import ChatResponse


class Chat:
    def __init__(self):
        pass
    
    @classmethod
    def classificator(cls,comment):
        
        prompt = f'''
          Você atuará como classificador de sentimentos. Cabe ressaltar que a Analise de sentimentos, há subtema de Polarização: tecnica que extrai sentimentos se é positivo, negativo ou neutro.
          voce irá classificar comentários coletados de uma postagem da rede social Instagram. Nesses comentários terá emojis, ou seja, podem indicar emoções, como ironia.
          
          caso haja algum comentário cuja o sentimento não seja identificável, classifique como "Neutro".
          observação: Não de justificativas e somente retorne apenas as palavras abaixo :
         
              Positivo
              Negativo
              Neutro
        
          comentario coletado : {comment}

        '''
        
        response: ChatResponse = chat(model='llama3', messages=[
                  {
                    'role': 'user',
                    'content': prompt,
                  },
                ])
        return response['message']['content']
