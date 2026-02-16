#RAFAEL LUIZ CUYPERS
#VINICIUS RODRIGUES DA COSTA
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

class ProdutoView:
    def __init__(self, root, controller):
        self.controller = controller

        # Configurações da janela
        root.title('Sistema de Cadastro de Produtos')
        root.geometry('1166x718')
        root.minsize(800, 600)

        # Imagem de fundo
        self.bg_frame = Image.open('background1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(root, image=self.bg_photo)
        self.bg_panel.image = self.bg_photo
        self.bg_panel.place(relwidth=1, relheight=1)

        # Frame do Formulário de Produtos
        self.prod_frame = tk.Frame(root, bg='#040405')
        self.prod_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Título
        self.txt = "CADASTRO DE PRODUTOS"
        self.heading = tk.Label(self.prod_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white')
        self.heading.pack(pady=20)

        # Campo Nome do Produto
        self.texto1 = tk.Label(self.prod_frame, text="Nome do Produto", bg="#040405", fg="white", font=("yu gothic ui", 13, "bold"))
        self.texto1.pack()
        self.entry_nome = tk.Entry(self.prod_frame, bg="white", font=("Arial", 12), bd=0)
        self.entry_nome.pack(pady=10, padx=20, ipadx=20, ipady=5)

        # Campo Quantidade
        self.texto2 = tk.Label(self.prod_frame, text="Quantidade", bg="#040405", fg="white", font=("yu gothic ui", 13, "bold"))
        self.texto2.pack()
        self.entry_quantidade = tk.Entry(self.prod_frame, bg="white", font=("Arial", 12), bd=0)
        self.entry_quantidade.pack(pady=10, padx=20, ipadx=20, ipady=5)

        # Campo Preço
        self.texto3 = tk.Label(self.prod_frame, text="Preço", bg="#040405", fg="white", font=("yu gothic ui", 13, "bold"))
        self.texto3.pack()
        self.entry_preco = tk.Entry(self.prod_frame, bg="white", font=("Arial", 12), bd=0)
        self.entry_preco.pack(pady=10, padx=20, ipadx=20, ipady=5)

        # Botão Adicionar Produto
        self.botao_adicionar = tk.Button(self.prod_frame, text="Adicionar Produto", bg="white", fg="black", font=("yu gothic ui", 13, "bold"), command=self.controller.adicionar_produto)
        self.botao_adicionar.pack(pady=20)

        # Botão Salvar Produto
        self.botao_salvar = tk.Button(self.prod_frame, text="Salvar Dados", bg="white", fg="black", font=("yu gothic ui", 13, "bold"), command=self.controller.salvar_produtos)
        self.botao_salvar.pack(pady=20)

        # Tabela de Produtos
        self.tree = ttk.Treeview(self.prod_frame, columns=('Nome', 'Quantidade', 'Preço'), show='headings')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Quantidade', text='Quantidade')
        self.tree.heading('Preço', text='Preço')
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

    def obter_dados_produto(self):
        # Obtém os dados dos campos de entrada
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        preco = self.entry_preco.get()
        return nome, quantidade, preco

    def limpar_campos(self):
        # Limpa os campos de entrada
        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def mostrar_mensagem(self, titulo, mensagem, tipo="info"):
        # Mostra uma mensagem para o usuário
        if tipo == "info":
            messagebox.showinfo(titulo, mensagem)
        elif tipo == "erro":
            messagebox.showerror(titulo, mensagem)

    def atualizar_tabela(self, produtos):
        # Atualiza a tabela de produtos com os dados fornecidos
        for row in self.tree.get_children():
            self.tree.delete(row)
        for produto in produtos:
            self.tree.insert('', tk.END, values=(produto['nome'], produto['quantidade'], f"{produto['preco']:.2f}"))
