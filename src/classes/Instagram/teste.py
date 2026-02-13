
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# --- CORREÇÃO AQUI ---
# Isso mantém a janela aberta mesmo após o fim do script
options.add_experimental_option("detach", True)
# ---------------------

# 1. Remove a flag de automação
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 2. Muda o User-Agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 3. Desabilita a detecção do Blink
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# Truque do navigator.webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://www.instagram.com/p/DUjMMjpEn7j/")