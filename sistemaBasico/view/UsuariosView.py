from tkinter import *
from tkinter import ttk


class ViewUsuario:

 root = Tk()
 root.title("Cadastro de Usuários")
 root.geometry("720x500")

 janelaPrincipal = ttk.Frame(root, padding=20)
 janelaPrincipal.grid(sticky="nsew")


 ttk.Label(janelaPrincipal, text="Cadastro de Usuários", font="Arial 15").grid(column=0, row=0, columnspan=2, pady=10)


 ttk.Label(janelaPrincipal, text="Nome:", font="Arial 10").grid(column=0, row=1, sticky="w", pady=5)
 nomeEntry = ttk.Entry(janelaPrincipal, width=30)
 nomeEntry.grid(column=0, row=2, sticky="w", pady=5)

 ttk.Label(janelaPrincipal, text="Sobrenome:", font="Arial 10").grid(column=1, row=1, sticky="w", pady=5)
 sobrenomeEntry = ttk.Entry(janelaPrincipal, width=30)
 sobrenomeEntry.grid(column=1, row=2, sticky="w", pady=5)


 ttk.Label(janelaPrincipal, text="Idade:", font="Arial 10").grid(column=0, row=3, sticky="w", pady=5)
 idadeEntry = ttk.Entry(janelaPrincipal, width=10)
 idadeEntry.grid(column=0, row=4, sticky="w", pady=5)

 ttk.Label(janelaPrincipal, text="Data de Nascimento:", font="Arial 10").grid(column=1, row=3, sticky="w", pady=5)
 dataNascimentoEntry = ttk.Entry(janelaPrincipal, width=20)
 dataNascimentoEntry.grid(column=1, row=4, sticky="w", pady=5)


 ttk.Label(janelaPrincipal, text="Email:", font="Arial 10").grid(column=0, row=5, sticky="w", pady=5)
 emailEntry = ttk.Entry(janelaPrincipal, width=40)
 emailEntry.grid(column=0, row=6, columnspan=2, sticky="we", pady=5)


 ttk.Label(janelaPrincipal, text="Senha:", font="Arial 10").grid(column=0, row=7, sticky="w", pady=5)
 senhaEntry = ttk.Entry(janelaPrincipal, width=20, show="*")
 senhaEntry.grid(column=0, row=8, sticky="w", pady=5)


 botaoSalvar = ttk.Button(janelaPrincipal, width=15, text="Cadastrar")
 botaoSalvar.grid(column=0, row=9, columnspan=2, pady=20)

 root.mainloop()

 
 
 
 
 
 
 
 


 
 
