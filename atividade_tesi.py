from email import message
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview Tabela")
        self.janela.geometry('460x300')
        self.frm_botoes = tk.Frame(self.janela)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(
            self.janela, show='headings', columns=colunas, height=5)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text="Nome")
        self.tvw.heading('cpf', text="CPF")
        self.tvw.heading('email', text="Email")

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('email', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=(
            'Manoel', '0000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end', values=(
            'Manoel', '0000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end', values=(
            'Manoel', '0000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end', values=(
            'Limeira', '1111111111', 'limeira@ufac.br'))
        self.tvw.insert('', 'end', values=(
            'Limeira', '1111111111', 'limeira@ufac.br'))
        self.tvw.insert('', 'end', values=(
            'Limeira', '1111111111', 'limeira@ufac.br'))

        self.scr = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

        # botoes
        self.btn_cadastrar = tk.Button(
            self.frm_botoes, text='Cadastrar', command=self.tela_cadastrar)
        self.btn_cadastrar.pack(side=tk.LEFT)
        #self.btn_deletar = tk.Button(self.frm_botoes, text='Deletar', command=self.deletar_selecionado)
        # self.btn_deletar.pack(side=tk.LEFT)

        self.btn_deletar_todos = tk.Button(
            self.frm_botoes, text='Deletar Todos', command=self.deletar_todos)
        self.btn_deletar_todos.pack(side=tk.LEFT)
        self.btn_deletar_lista = tk.Button(
            self.frm_botoes, text='Deletar Selecionados', command=self.deletar_lista)
        self.btn_deletar_lista.pack(side=tk.LEFT)

        self.btn_atualizar = tk.Button(
            self.frm_botoes, text='Atualizar', command=self.tela_atualizar)
        self.btn_atualizar.pack(side=tk.LEFT)

    def tela_atualizar(self):
        # pegando informações do treeview
        selecionado = self.tvw.selection()
        contador = 0
        contador = contador + len(self.tvw.selection())
        if contador > 1:
            messagebox.showerror("Erro!", "Selecione apenas um usuário!")

        elif contador == 1:
            self.top_atualizar = tk.Toplevel()
            self.top_atualizar.grab_set()
            self.top_atualizar.title('Atualizar')
            self.top_atualizar.geometry('300x200')
            self.lbl_nome = tk.Label(self.top_atualizar, text='Nome:')
            self.lbl_nome.grid(row=0, column=0)
            self.lbl_cpf = tk.Label(self.top_atualizar, text='CPF:')
            self.lbl_cpf.grid(row=1, column=0)
            self.lbl_email = tk.Label(self.top_atualizar, text='Email:')
            self.lbl_email.grid(row=2, column=0)

            lista = self.tvw.item(selecionado, 'values')
            self.ent_nome = tk.Entry(self.top_atualizar, width=30)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert(0, lista[0])

            self.ent_cpf = tk.Entry(self.top_atualizar, width=30)
            self.ent_cpf.grid(row=1, column=1)
            self.ent_cpf.insert(0, lista[1])

            self.ent_email = tk.Entry(self.top_atualizar, width=30)
            self.ent_email.grid(row=2, column=1)
            self.ent_email.insert(0, lista[2])

            lista = self.tvw.item(selecionado, 'values')
            self.ent_nome = tk.Entry(self.top_atualizar, width=30)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert(0, lista[0])

            self.ent_cpf = tk.Entry(self.top_atualizar, width=30)
            self.ent_cpf.grid(row=1, column=1)
            self.ent_cpf.insert(0, lista[1])

            self.ent_email = tk.Entry(self.top_atualizar, width=30)
            self.ent_email.grid(row=2, column=1)
            self.ent_email.insert(0, lista[2])

            self.btn_confirmar = tk.Button(
                self.top_atualizar, text='Confirmar Atualização', command=self.confirmar_atualiza)
            self.btn_confirmar.grid(row=3, column=1)

        else:
            messagebox.showwarning("Erro!", "Nenhum usuário selecionado!")

    def confirmar_atualiza(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        selecionado = self.tvw.selection()
        self.tvw.item(selecionado, values=(nome, cpf, email))
        self.top_atualizar.destroy()
        self.janela.deiconify()

    def deletar_todos(self):
        var = messagebox.askquestion("Cuidado", "Você está certo disso?")
        if var == "yes":
            todos = self.tvw.get_children()
            for t in todos:
                self.tvw.delete(t)

    def deletar_lista(self):
        lista = self.tvw.selection()
        for l in lista:
            self.tvw.delete(l)

    def deletar_selecionado(self):
        selecionado = self.tvw.selection()
        self.tvw.delete(selecionado)

    def tela_cadastrar(self):
        self.top_cadastro = tk.Toplevel()
        # self.janela.withdraw()
        self.top_cadastro.grab_set()
        self.top_cadastro.title('Cadastro')
        self.top_cadastro.geometry('300x200')
        self.lbl_nome = tk.Label(self.top_cadastro, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_cpf = tk.Label(self.top_cadastro, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0)
        self.lbl_email = tk.Label(self.top_cadastro, text='Email:')
        self.lbl_email.grid(row=2, column=0)
        self.ent_nome = tk.Entry(self.top_cadastro, width=30)
        self.ent_nome.grid(row=0, column=1)
        self.ent_cpf = tk.Entry(self.top_cadastro, width=30)
        self.ent_cpf.grid(row=1, column=1)
        self.ent_email = tk.Entry(self.top_cadastro, width=30)
        self.ent_email.grid(row=2, column=1)
        self.btn_confirmar = tk.Button(
            self.top_cadastro, text='Confirmar', command=self.confirmar_cadastro)
        self.btn_confirmar.grid(row=3, column=1)

    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        if nome == '' or cpf == '' or email == '':
            messagebox.showinfo(
                'Aviso', 'Todos campos são obrigatórios', parent=self.top_cadastro)
        else:
            self.tvw.insert('', 'end', values=(nome, cpf, email))
            self.top_cadastro.destroy()
            self.janela.deiconify()


app = tk.Tk()
Tela(app)
app.mainloop()
