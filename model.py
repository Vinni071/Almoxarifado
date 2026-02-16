#RAFAEL LUIZ CUYPERS
#VINICIUS RODRIGUES DA COSTA
import pickle  # biblioteca para serialização/deserialização de objetos Python
import os  # biblioteca para operações do sistema operacional

class ProdutoModel:
    def __init__(self):
        self.produtos = []  # Inicializa uma lista vazia para armazenar os produtos

    def adicionar_produto(self, nome, quantidade, preco):
        produto = {'nome': nome, 'quantidade': int(quantidade), 'preco': float(preco)}
        self.produtos.append(produto)  # Adiciona um dicionário representando o produto à lista de produtos
    
    def obter_produtos(self):
        return self.produtos  # Retorna a lista de produtos

    def salvar_dados(self, caminho):
        # Abre um arquivo em modo de escrita binária e salva a lista de produtos
        with open(caminho, 'wb') as arquivo:
            pickle.dump(self.produtos, arquivo)
    
    def carregar_dados(self, caminho):
        # Verifica se o arquivo existe e carrega os dados a partir dele
        if os.path.exists(caminho):
            with open(caminho, 'rb') as arquivo:
                self.produtos = pickle.load(arquivo)
