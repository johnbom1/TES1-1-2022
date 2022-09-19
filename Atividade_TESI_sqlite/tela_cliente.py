from cgitb import text
import tkinter as tk
from tkinter import messagebox, ttk
from turtle import width


import aula_banco as bd

class TelaCliente():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("400x400")
        self.frm = tk.Frame(self.janela)
        self.fbt = tk.Frame(self.janela)
        self.frm.pack()
        self.fbt.pack()

        self.lbl_nome = tk.Label(self.frm, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self.frm, width=40)
        self.ent_nome.grid(row=0, column=1)
        self.lbl_cpf = tk.Label(self.frm, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0)
        self.ent_cpf = tk.Entry(self.frm, width=40)
        self.ent_cpf.grid(row=1, column=1)

        self.btn_inserir = tk.Button(self.frm, text='Inserir', command=self.inserir)
        self.btn_inserir.grid(row=2, column=1)

        

        self.tvw = ttk.Treeview(self.frm, columns=('id', 'nome', 'cpf'), show='headings')
        self.tvw.column('id', width=30)
        self.tvw.column('nome', width=150)
        self.tvw.column('cpf', width=190)
        self.tvw.heading('id', text='ID')
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.grid(row=3, column=0, columnspan=2)
        self.atualizar_tvw()

        self.btn_remover = tk.Button(self.fbt, text='Remover', command=self.remover)
        self.btn_remover.grid(row=0, column=0)
        self.btn_atualizar = tk.Button(self.fbt, text='Atualizar', command=self.atualizar)
        self.btn_atualizar.grid(row=0, column=1)

        self.btn_confirmar = tk.Button(self.fbt, text='Confirmar', command=self.confirmar)
        self.btn_confirmar['state'] = tk.DISABLED
        self.btn_confirmar.grid(row=0, column=2)

        self.btn_cancelar = tk.Button(self.fbt, text='Cancelar', command=self.cancelar)
        self.btn_cancelar['state'] = tk.DISABLED
        self.btn_cancelar.grid(row=0, column=3)





    def atualizar_tvw(self):
        for i in self.tvw.get_children():
            self.tvw.delete(i)

        query = 'SELECT * FROM cliente;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw.insert('', tk.END, values=tupla)


    def inserir(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        sql_inserir = f'INSERT INTO cliente VALUES(NULL,"{nome}","{cpf}");'
        bd.inserir(sql_inserir)
        messagebox.showinfo('Aviso', 'Cliente inserido com sucesso')
        self.ent_nome.delete(0,'end')
        self.ent_cpf.delete(0, 'end')
        self.atualizar_tvw()

    def remover(self):
        selecionado = self.tvw.selection()
        id = self.tvw.item(selecionado, 'values')[0]
        query = f'DELETE FROM cliente WHERE id = {id};'
        bd.remover(query)
        self.atualizar_tvw()
        messagebox.showinfo('Aviso', 'Cliente removido com sucesso!')

    def atualizar(self):
        selecionado = self.tvw.selection()
        nome = self.tvw.item(selecionado, 'values')[1]
        cpf = self.tvw.item(selecionado, 'values')[2]
        self.ent_nome.insert(0, nome)
        self.ent_cpf.insert(0, cpf)
        self.btn_confirmar['state'] = tk.NORMAL
        self.btn_atualizar['state'] = tk.DISABLED
        self.btn_inserir['state'] = tk.DISABLED
        self.btn_cancelar['state'] = tk.NORMAL

    def confirmar(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        selecionado = self.tvw.selection()
        id = self.tvw.item(selecionado, 'values')[0]
        query = f'UPDATE cliente SET nome="{nome}", cpf="{cpf}" WHERE id={id};'
        bd.atualizar(query)
        messagebox.showinfo('Aviso', 'Cliente atualizado com sucesso!')
        self.btn_confirmar['state'] = tk.DISABLED
        self.btn_atualizar['state'] = tk.NORMAL
        self.btn_inserir['state'] = tk.DISABLED
        self.ent_nome.delete(0, 'end')
        self.ent_cpf.delete(0, 'end')
        self.atualizar_tvw()

    def cancelar(self):
        self.ent_nome.delete(0, 'end')
        self.ent_cpf.delete(0, 'end')
        
        self.btn_inserir['state'] = tk.NORMAL
        self.btn_atualizar['state'] = tk.NORMAL
        self.btn_cancelar['state'] = tk.DISABLED
        self.btn_confirmar['state'] = tk.DISABLED




app = tk.Tk()
TelaCliente(app)
app.mainloop()