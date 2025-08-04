from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

navegador = webdriver.Chrome()

#Lista para armazenar os produtos.
itens = []

#Url que seram acessadas.
urls = ['https://store.vonixx.com.br/lava-autos',
       'https://store.vonixx.com.br/descontaminacao',
        'https://store.vonixx.com.br/acessorios']

#Percorre todoas as urls passadas.
for url in urls:
    navegador.get(url)
    sleep(3)

    produtos = navegador.find_elements(By.XPATH, '//li[contains(@class,"item")]')

    # Loop para percorrer e slavar todos os profutos dentro da lista [itens].
    for produto in produtos:
        try:
            titulo = produto.find_element(By.XPATH, './/div[contains(@class,"product-name")]').text.strip()
            preco = produto.find_element(By.XPATH, './/span[contains(@class,"price-off")]').text.strip()
            itens.append({"Produto": titulo, "Valor": preco})
        except Exception as e:
            continue  # Mesmo que não tenha Título ou Preço vai seguir.

#Deixa o navegador em tela cheiaa.
navegador.maximize_window()

#Espera o navegar carregar.
sleep(5)

print(f'Foram encontrados: {len(itens)} produtos e adicionados a lista.')

#Lopp para moficiar todos os produtos encontrados.
for item in itens:
    print(f'{item["Produto"]}  {item["Valor"]}')

#Armazenar os dados em formato de tabela.
df = pd.DataFrame(itens)

#Criando um arquivo em excel para salvar os dados.
df.to_excel("Produtos.xlsx", index=False) # index=Flase significa não incluir os indíce dos produtos.

print("Arquivo 'Produtos.xlsx' criado com sucesso!")