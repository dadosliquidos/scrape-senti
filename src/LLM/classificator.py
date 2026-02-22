from ollama import chat
from ollama import ChatResponse


class Chat:
    def __init__(self):
        pass
    
    @classmethod
    def classificator(cls,comment):
        
        prompt = f'''
            
           Você é um sistema de classificação de sentimentos estrito. Siga esta ordem de prioridade lógica para classificar o texto abaixo:

        PASSO 1 - VERIFICAÇÃO DE CONTEÚDO (CRÍTICO):
        - O texto contém APENAS espaços em branco, quebras de linha ou é uma string vazia?
        -> Se SIM: Classifique IMEDIATAMENTE como "Outros" e pare.
        -> Se NÃO (ou seja, se houver qualquer letra, número, pontuação OU EMOJI): Continue para o Passo 2. NUNCA classifique como "Outros" se houver conteúdo visível.

        PASSO 2 - ANÁLISE DE SENTIMENTO:
        Classifique o conteúdo restante em uma destas 3 categorias:

        1. "Positivo": Elogios, concordância, emojis felizes/celebrativos.
        2. "Negativo": Críticas, reclamações, emojis de desagrado e IRONIA (ex: elogio sarcástico deve ser Negativo).
        3. "Neutro": Use estritamente para marcações de usuários (@usuario) sem texto adicional, perguntas factuais ou afirmações sem carga emocional. NÃO use esta categoria se houver qualquer adjetivo ou emoji expressivo.

        
        ENTRADA PARA ANÁLISE:
        Comentário: '{comment}'

        SAÍDA:
        Responda com apenas uma palavra (Positivo, Negativo, Neutro ou Outros). Sem pontuação.
        


        '''
        
        response: ChatResponse = chat(model='solar', messages=[
                  {
                    'role': 'user',
                    'content': prompt,
                  },
                ])
        return response['message']['content']
