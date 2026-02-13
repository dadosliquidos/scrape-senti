import os
import json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ast
import time





class Login:
    load_dotenv()
    def __init__(self):
        pass

    @classmethod    
    def inicializarNavegador(cls, url):
      #  options = webdriver.FirefoxOptions()
       # #options.add_argument("--headless")
       # navegador = webdriver.Firefox()
        #navegador.get(url)
        options = Options()

        options.add_experimental_option("detach", True)
# ---------------------

# 1. Remove a flag de automação
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

# 2. Muda o User-Agent
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 3. Desabilita a detecção do Blink
        options.add_argument("--disable-blink-features=AutomationControlled")
       

    
        navegador = webdriver.Chrome(options=options)

        navegador.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                 "source": """
                 Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                     })
                    """
})

        navegador.get(url)

        for i in range(1,9):
            string = 'COOKIE_{}'.format(i)

            cookie = os.getenv(string)
            cookie_formatado = ast.literal_eval(cookie)

            navegador.add_cookie(cookie_formatado)
        
        
        navegador.refresh()
        time.sleep(3)

        return navegador