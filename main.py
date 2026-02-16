#RAFAEL LUIZ CUYPERS
#VINICIUS RODRIGUES DA COSTA
import tkinter as tk
from model import ProdutoModel
from view import ProdutoView
from controller import ProdutoController
import os

if __name__ == "__main__":
    root = tk.Tk()
    
    model = ProdutoModel()
    controller = ProdutoController(model, None)
    view = ProdutoView(root, controller)
    controller.view = view

    # Carregar dados se o arquivo existir
    caminho_dados = 'produtos.pkl'
    if os.path.exists(caminho_dados):
        model.carregar_dados(caminho_dados)
        view.atualizar_tabela(model.obter_produtos())
    
    root.mainloop()
