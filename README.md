# 📊 Scrape-Senti

Um pipeline automatizado de Extração, Transformação e Carga (ETL) projetado para capturar comentários da rede social Instagram e realizar a classificação de sentimentos utilizando Small Language Models (SLMs) executados localmente. 

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC) em Sistemas de Informação, focando em arquitetura de dados, privacidade (inferência *on-premise* sem dependência de APIs de terceiros) e modelagem dimensional para *Business Intelligence* (BI).

---

## 🚀 Principais Funcionalidades

* **Web Scraping Dinâmico:** Robô construído com Selenium capaz de lidar com rolagem infinita (infinite scroll) e renderização assíncrona (AJAX) para coletar comentários em larga escala.
* **Autenticação Segura:** Sistema de injeção de *cookies* via variáveis de ambiente (`.env`) para contornar bloqueios de login sem expor credenciais no código-fonte.
* **Análise de Sentimento com IA Local:** Integração com o [Ollama](https://ollama.com/) para executar modelos de linguagem de pequeno porte (Gemma 2, Qwen 2.5, Ministral-3) diretamente na máquina local, classificando os textos em Positivo, Negativo, Neutro ou Outros.
* **Data Warehousing:** Armazenamento transacional (OLTP) para a coleta bruta e carga em um modelo dimensional *Star Schema* (OLAP) utilizando MySQL.
* **Visualização de Dados (BI):** Geração de gráficos estatísticos e nuvens de palavras (WordClouds) utilizando Pandas e Matplotlib para identificação visual de tendências e emojis mais utilizados.

---

## 🏗️ Arquitetura do Sistema (Fluxo ETL)

1. **Extract (Extração):** O *crawler* em Python navega pela URL alvo do Instagram, injeta os cookies de sessão, carrega o DOM dinamicamente e captura o HTML estático usando BeautifulSoup.
2. **Transform (Transformação):** Os dados textuais brutos são higienizados (remoção de quebras de linha, escape de caracteres especiais para o banco) e enviados via *prompt engineering* para o SLM local (via Ollama), que devolve a classificação do sentimento.
3. **Load (Carga):** Os dados enriquecidos são persistidos inicialmente em tabelas transacionais e, posteriormente, distribuídos em uma estrutura de Data Warehouse (Tabela de Fatos e Dimensões) no MySQL.

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Automação e Raspagem:** Selenium WebDriver, BeautifulSoup4
* **Banco de Dados:** MySQL
* **Inteligência Artificial:** Ollama (modelos *open source*: `gemma2:9b`, `qwen2.5:7b`, `ministral-3:8b`)
* **Análise e Visualização:** Pandas, Matplotlib, WordCloud, tqdm
* **Gerenciamento de Ambiente:** python-dotenv

---

## ⚙️ Pré-requisitos e Instalação

Antes de iniciar, certifique-se de ter o [Python](https://www.python.org/), o [MySQL Server](https://dev.mysql.com/downloads/mysql/) e o [Ollama](https://ollama.com/download) instalados em sua máquina. Você também precisará do navegador Mozilla Firefox instalado para o webdriver.

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/scrape-senti.git](https://github.com/seu-usuario/scrape-senti.git)
cd scrape-senti