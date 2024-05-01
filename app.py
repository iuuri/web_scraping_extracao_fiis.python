from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from openpyxl import Workbook

#variavel do selenium para configurar o webdriver no navagador. Fazendo com esses passos não precisa baixar o driver na maquina.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#acessar o site fundamentus
url_site = 'https://fundamentus.com.br/fii_resultado.php'
driver.get(url_site)

#localiza tabela
local_tabela = 'tabelaResultado'
elemento_tabela = driver.find_element('id', local_tabela)

#visualiza conteudo de dentro da tabela com o outerHTML
html_tabela = elemento_tabela.get_attribute("outerHTML")

#transforma o conteudo em string e converte "." para ","
tabela = pd.read_html(str(html_tabela), thousands=".", decimal=",")[0]

# Salvar os dados em um arquivo Excel
nome_arquivo = 'fiis.xlsx'
tabela.to_excel(nome_arquivo, index=False)
print(f'Dados salvos em {nome_arquivo}')
