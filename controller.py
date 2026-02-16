#RAFAEL LUIZ CUYPERS
#VINICIUS RODRIGUES DA COSTA
class ProdutoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def adicionar_produto(self):
        # Obtém os dados do produto a partir da visualização
        nome, quantidade, preco = self.view.obter_dados_produto()
        if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit():
            # Adiciona o produto ao modelo e atualiza a tabela
            self.model.adicionar_produto(nome, quantidade, preco)
            self.view.atualizar_tabela(self.model.obter_produtos())
            self.view.mostrar_mensagem("Sucesso", "Produto adicionado com sucesso!")
            self.view.limpar_campos()
        else:
            # Mostra uma mensagem de erro se os dados forem inválidos
            self.view.mostrar_mensagem("Erro", "Por favor, insira dados válidos.", tipo="erro")

    def salvar_produtos(self):
        # Salva os dados dos produtos em um arquivo
        caminho = 'produtos.pkl'
        self.model.salvar_dados(caminho)
        self.view.mostrar_mensagem("Sucesso", "Dados salvos com sucesso!")
