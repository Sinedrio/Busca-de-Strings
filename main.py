from tkinter import *
from tkinter import scrolledtext

janela = Tk()
janela.title("Buscando as palavras")
janela.geometry("900x900")

def buscar():
    txt.delete(0.1, END)
    frequencia.delete(0, END)
    palavra = palavraEntrada.get()
    i = 0
    arquivo = open("chat (1).txt", "r")
    for line in arquivo:
        line.strip().split('\n')
        if palavra in line:
            i += 1
            txt.insert(INSERT, line + '\n')
    frequencia.insert(0, i)
    arquivo.close()

# cria as labels
palavra = Label(janela, text="Palavra que deseja pesquisar: ", font=("Arial", 14))
palavra.place(relx=0.05, rely=0.08)

quantidade = Label(janela, text="Frequência total da palavra: ", font=("Arial", 14))
quantidade.place(relx=0.05, rely=0.15)

# cria as entradas (entry)
palavraEntrada = Entry(janela, width=15, font=("Arial", 14))
palavraEntrada.place(relx=0.25, rely=0.08)

frequencia = Entry(janela, width=15, font=("Arial", 14))
frequencia.place(relx=0.25, rely=0.15)

# cria o scrolledtext
txt = scrolledtext.ScrolledText(janela, width=100, height=20)
txt.place(relx=0.05, rely=0.35)



pesquisar = Button(janela, text="Pesquisar", command=buscar)
pesquisar.place(relx=0.5, rely=0.08)

janela.mainloop()