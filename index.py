import pandas as pd

from bs4 import BeautifulSoup

with open('index.html', 'r') as arquivo:
    conteudo = arquivo.read()

soup = BeautifulSoup(conteudo, 'html.parser')

tabela = soup.find('table')

linhas = tabela.find_all('tr')

produtos = []
precos = []

quantidades = []
faturamentos = []

for linha in linhas[1:]:

    colunas = linha.find_all('td')
    nome = colunas[0].get_text()

    preco = float(colunas[1].get_text())
    quantidade = int(colunas[2].get_text())
    faturamento = preco * quantidade

    produtos.append(nome)
    precos.append(preco)
    quantidades.append(quantidade)
    faturamentos.append(faturamento)

df = pd.DataFrame({'Produto': produtos, 'Preço': precos, 'Quantidade': quantidades, 'Faturamento': faturamentos})

print(df)