from tkinter import *
from playsound import playsound
from gtts import *
import os

root = Tk()
root.title('Conversor de Texto para Fala')
root.geometry('500x420')
root.maxsize(500, 420)
root.minsize(500, 420)
root.configure(bg='#1d1d1d')

def margem(altura):
    tela = Canvas(  root,
                    width=500,
                    height=altura,
                    bg='#1d1d1d',
                    bd=0,
                    highlightthickness=0,
                    relief='ridge')
    tela.pack()

def botao(texto, comando, padX):
    botao = Button( root,
                    text = texto,
                    padx = padX,
                    pady = 20,
                    command = comando,
                    fg='#ffffff',
                    activeforeground='#ffffff',
                    bg='#c69749',
                    activebackground='#c69749',
                    relief=FLAT,
                    font=('Montserrat', 12, 'bold'))
    botao.pack()

def inicia():
    texto_inserido = entrada.get()
    fala = gTTS(text = texto_inserido, 
                lang='pt', 
                tld='com.br')
    arquivo_fala = 'arquivo_fala.mp3'
    fala.save('arquivo_fala.mp3')
    playsound(arquivo_fala)

def limpa():
    entrada.delete(0, END)
    os.remove('arquivo_fala.mp3')

margem(20)

titulo = Label (root, 
                bg='#1d1d1d', 
                fg='#ffffff', 
                font=('Montserrat', 18, 'bold'), 
                text='Conversor de Texto para Fala')

titulo.pack()

margem(40)

insere_texto = Label (root, 
                bg='#1d1d1d', 
                fg='#ffffff', 
                font=('Montserrat', 16), 
                text='Insira o seu texto:')
insere_texto.pack()

margem(40)

entrada = Entry(root, 
                width=25, 
                borderwidth=4,
                border=0, 
                relief=FLAT, 
                foreground='#ffffff',
                bg='#000000',
                font=('Montserrat', 21, 'bold'),
                justify=CENTER
                )
entrada.pack()

margem(20)
botao('INICIAR', inicia, 37)
margem(10)
botao('LIMPAR', limpa, 37)
root.mainloop()