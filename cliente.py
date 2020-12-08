# PROJETO CRIADO A PARTIR DO CÓDIGO DISPONIBILIZADO POR:
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)

#AUTORAS DO PROJETO: ALEIKA ALVES E TAYNA ARRUDA

# importacao das bibliotecas
from socket import * # sockets
import threading
from tkinter import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 61001 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM)  # criacao do socket UDP
                                            # AF_INET - familia de endereços (Familia IP)
                                            # SOCK_DGRAM - tipo de serviço (datagrama)

def painelDeControle(window):
    global verde
    global laranja
    global lavanda
    global azul

    botaoAumentarVelocTremVerde = Button(window, text="+ 0.1", bg='green', command=lambda: aumentarVelocidade(verde))
    botaoDiminuirVelocTremVerde = Button(window, text=" - 0.1 ", bg='green', command= lambda: diminuirVelocidade(verde))
    botaoAumentarVelocTremVerde.place(x = 20, y = 50)
    botaoDiminuirVelocTremVerde.place(x = 20, y = 100)

    botaoAumentarVelocTremLavanda= Button(window, text="+ 0.1", bg='purple', command=lambda: aumentarVelocidade(lavanda))
    botaoDiminuirVelocTremLavanda = Button(window, text=" - 0.1 ", bg='purple', command= lambda: diminuirVelocidade(lavanda))
    botaoAumentarVelocTremLavanda.place(x = 120, y = 50)
    botaoDiminuirVelocTremLavanda.place(x = 120, y = 100)

    botaoAumentarVelocTremLaranja= Button(window, text="+ 0.1", bg='orange', command= lambda: aumentarVelocidade(laranja))
    botaoDiminuirVelocTremLaranja = Button(window, text=" - 0.1 ", bg='orange', command=lambda: diminuirVelocidade(laranja))
    botaoAumentarVelocTremLaranja.place(x = 220, y = 50)
    botaoDiminuirVelocTremLaranja.place(x = 220, y = 100)

    botaoAumentarVelocTremAzul= Button(window, text="+ 0.1", bg='blue', command=lambda: aumentarVelocidade(azul))
    botaoDiminuirVelocTremAzul = Button(window, text=" - 0.1 ", bg='blue', command=lambda: diminuirVelocidade(azul))
    botaoAumentarVelocTremAzul.place(x = 320, y = 50)
    botaoDiminuirVelocTremAzul.place(x = 320, y = 100)


def aumentarVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremLavanda
    global velocidadeTremLaranja
    global velocidadeTremAzul
    global verde
    global laranja
    global lavanda
    global azul


    if(trem == verde):
        if(velocidadeTremVerde < 0.1 or velocidadeTremVerde == 0.1):
            velocidadeTremVerde = round(velocidadeTremVerde - 0.01, 2)
            if(velocidadeTremVerde == 0):
                velocidadeTremVerde = 0.01
        else:
            velocidadeTremVerde = round(velocidadeTremVerde - 0.1, 1)
    elif (trem == laranja):
        if(velocidadeTremLaranja == 0.1):
            velocidadeTremLaranja = round(velocidadeTremLaranja - 0.01, 2)
            if(velocidadeTremLaranja == 0):
                velocidadeTremLaranja = 0.01
        else:
            velocidadeTremLaranja = round(velocidadeTremLaranja - 0.1, 1)
    elif (trem == lavanda):
        if(velocidadeTremLavanda == 0.1):
            velocidadeTremLavanda = round(velocidadeTremLavanda - 0.01, 2)
            if(velocidadeTremLavanda == 0):
                velocidadeTremLavanda = 0.01
        else:
            velocidadeTremLavanda = round(velocidadeTremLavanda - 0.1, 1)
    elif (trem == azul):
        if(velocidadeTremAzul == 0.1):
            velocidadeTremAzul = round(velocidadeTremAzul - 0.01, 2)
            if(velocidadeTremAzul == 0):
                velocidadeTremAzul = 0.01
        else:
            velocidadeTremAzul = round(velocidadeTremAzul - 0.1, 1)
    else:
        print("cor inválida!")
    
    enviarVelocidade()


def diminuirVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremLavanda
    global velocidadeTremLaranja
    global velocidadeTremAzul
    global verde
    global laranja
    global lavanda
    global azul

    if(trem == verde):
        if(velocidadeTremVerde == 2):
            velocidadeTremVerde = 2
        else:
            velocidadeTremVerde = round(velocidadeTremVerde + 0.1, 1)
    elif (trem == laranja):
        if(velocidadeTremLaranja == 2):
            velocidadeTremLaranja = 2
        else:
            velocidadeTremLaranja = round(velocidadeTremLaranja + 0.1, 1)
    elif (trem == lavanda):
        if(velocidadeTremLavanda == 2):
            velocidadeTremLavanda = 2
        else:
            velocidadeTremLavanda = round(velocidadeTremLavanda + 0.1, 1)
    elif (trem == azul):
        if(velocidadeTremAzul == 2):
            velocidadeTremAzul = 2
        else:
            velocidadeTremAzul = round(velocidadeTremAzul + 0.1, 1)
    else:
        print("cor inválida!")
    
    enviarVelocidade()


def enviarVelocidade():
    global velocidadeTremVerde
    global velocidadeTremLavanda
    global velocidadeTremLaranja
    global velocidadeTremAzul

    message = str(velocidadeTremVerde) + "|" + str(velocidadeTremLavanda) + "|" + str(velocidadeTremLaranja) + "|" + str(velocidadeTremAzul)
    clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor

# variaveis que identificam qual o trem atraves de um valor int
verde = 1 
lavanda = 2
laranja = 3
azul = 4

#variaveis que controlam a velocidade dos trens
velocidadeTremVerde = 1
velocidadeTremLavanda = 1
velocidadeTremLaranja = 1
velocidadeTremAzul = 1

window = Tk()
window.title("Painel de Controle")
canvas = Canvas(window, width=400, height=200)
canvas.pack()

threadPainelDeControle = threading.Thread(target=painelDeControle, args=[window] )

threadPainelDeControle.start()

window.mainloop()

threadPainelDeControle.join()

clientSocket.close() # encerra o socket do cliente
