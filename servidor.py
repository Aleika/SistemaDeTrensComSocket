# PROJETO CRIADO A PARTIR DO CÓDIGO DISPONIBILIZADO POR:
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)

#AUTORAS DO PROJETO: ALEIKA ALVES E TAYNA ARRUDA

from socket import * # sockets
import threading
from tkinter import *
import time

def visualizarPosicaoDosTrens(window):
    window.geometry("400x300")    

    trilhoVerde = canvas.create_rectangle(20, 20, 120, 120, outline="green", width="10")
    trilhoLavanda = canvas.create_rectangle(150, 20, 250, 120, outline="purple", width="10")
    trilhoLaranja = canvas.create_rectangle(280, 20, 380, 120, outline="orange", width="10")
    trilhoAzul = canvas.create_rectangle(20, 150, 380, 250, outline="blue", width="10")

def trilhoVerde(window, canvas):
    global velocidadeTremVerde
    global l1 
    global l2
    global l3 
    global l4 
    global mutexL2L8

    tremVerde = canvas.create_rectangle(10, 10, 30, 30, fill="white")

    while(1):
        if(l1<10):
            canvas.move(tremVerde, 10, 0)   
            l1 = l1+1
            l2 =0
        else:
            if (l2 < 10):
                if(l2 == 0):
                    sem1.acquire()
                    mutexL2L8.acquire()
                canvas.move(tremVerde, 0, 10) 
                l2=l2+1
            else:
                if(l2 == 10):
                    mutexL2L8.release()
                    sem1.release()
                    l2=l2+1
                if (l3 < 10):
                    if(l2 == 11):
                        mutexL3L13.acquire()
                        l2 = l2 +1
                    canvas.move(tremVerde, -10, 0) 
                    l3=l3+1 
                else:
                    if(l3 == 10):
                        mutexL3L13.release()
                        l3 = l3 +1
                    if (l4 < 10):
                        canvas.move(tremVerde, 0, -10) 
                        l4=l4+1
                    else:
                        l1=0
                        l2=0
                        l3=0
                        l4=0
        time.sleep(velocidadeTremVerde)

def trilhoLavanda(window, canvas):
    global mutexL2L8
    global mutexL6L12
    global l5
    global l6
    global l7
    global l8
    global velocidadeTremLavanda

    tremLavanda = canvas.create_rectangle(140, 10, 160, 30, fill="white")

    while(1):
        if(l5<10):
            canvas.move(tremLavanda, 10, 0)   
            l5 = l5+1
        else:
            if(l5 == 10):
                sem2.acquire()
                mutexL6L12.acquire()
                l5 = l5 +1
            if (l6 < 10):
                canvas.move(tremLavanda, 0, 10) 
                l6=l6+1
            else:
                if(l6 == 10):
                    mutexL6L12.release()
                    sem2.release()
                    l6 = l6 +1
                if(l7 < 10):
                    if(l7 == 0):
                        sem1.acquire()
                        mutexL7L14.acquire()
                    canvas.move(tremLavanda, -10, 0) 
                    l7=l7+1
                    l8 = 0
                else:
                    if(l8<10):
                        if(l8 == 0):
                            mutexL2L8.acquire()
                            mutexL7L14.release()
                            sem1.release()
                        canvas.move(tremLavanda, 0, -10) 
                        l8=l8+1
                    else:
                        if(l8 == 10):
                            mutexL2L8.release()
                            l8=l8+1
                        l5=0
                        l6=0
                        l7=0
                        l8=0
        time.sleep(velocidadeTremLavanda)
       
def trilhoLaranja(window, canvas):
    global l9
    global l10
    global l11
    global l12
    global mutexL6L12
    global velocidadeTremLaranja

    tremLaranja = canvas.create_rectangle(270, 10, 290, 30, fill="white")

    while(1):
        if(l9<10):
            canvas.move(tremLaranja, 10, 0)   
            l9 = l9+1
        elif (l10 < 10):
            canvas.move(tremLaranja, 0, 10) 
            l10=l10+1
        elif (l11 < 10):
            if(l11 == 0):
                sem2.acquire()
                mutexL11L15.acquire()
            canvas.move(tremLaranja, -10, 0) 
            l11=l11+1
        elif (l12< 10):
            if(l11 == 10):
                mutexL6L12.acquire()
                mutexL11L15.release()
                sem2.release()
                l11 = l11+1
            canvas.move(tremLaranja, 0, -10) 
            l12=l12+1
        else:
            if(l12 == 10):
                mutexL6L12.release()
                l12 = l12 + 1
            l9=0
            l10=0
            l11=0
            l12=0
        time.sleep(velocidadeTremLaranja)  

def trilhoAzul(window, canvas):
    global l13
    global l14
    global l15
    global l16
    global l17
    global l18
    global velocidadeTremAzul

    tremLaranja = canvas.create_rectangle(10, 140, 30, 160, fill="white")

    while(1):
        if(l13<12):
            if(l13 == 0):
                sem1.acquire()
                mutexL3L13.acquire()
            canvas.move(tremLaranja, 10, 0)   
            l13 = l13+1
        else:
            if(l13==12):
                mutexL3L13.release()
                sem1.release()
                l14=13
                l13=l13+1
            if(l14 > 12 and l14 < 24):
                if(l14 == 13):
                    sem2.acquire()
                    mutexL7L14.acquire()
                canvas.move(tremLaranja, 10, 0) 
                l14=l14+1
            else:
                if(l14==24):
                    mutexL7L14.release()
                    sem2.release()
                    l15=25
                    l14=l14+1
                if(l15>24 and l15<38):
                    if(l15 == 25):
                        mutexL11L15.acquire()
                    canvas.move(tremLaranja, 10, 0) 
                    l15=l15+1
                    l16=0
                else:
                    if(l16 == 0):
                        mutexL11L15.release()
                    if(l16<10):
                        canvas.move(tremLaranja, 0, 10) 
                        l16=l16+1
                        l17=0
                    else:
                        if(l17<36):
                            canvas.move(tremLaranja, -10, 0) 
                            l17=l17+1
                        else:
                            if(l18<10):
                                canvas.move(tremLaranja, 0, -10)
                                l18=l18+1
                            else:
                                l13=0 
                                l14=0
                                l15=0
                                l16=0
                                l17=0
                                l18=0        
        time.sleep(velocidadeTremAzul)
   
def comunicacaoComCliente():
    global serverSocket
    global velocidadeTremVerde
    global velocidadeTremLaranja
    global velocidadeTremLavanda
    global velocidadeTremAzul

    while 1:
        message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
        
        velocidadeTremVerde = float(message.decode('utf-8').split('|')[0])
        velocidadeTremLavanda = float(message.decode('utf-8').split('|')[1])
        velocidadeTremLaranja = float(message.decode('utf-8').split('|')[2])
        velocidadeTremAzul = float(message.decode('utf-8').split('|')[3])
        
# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61001 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
                                            # o bind associa o socket criado a porta local do sistema operacional
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))

i = 0

#criação / inicialização dos mutex
mutexL2L8 = threading.Lock()
mutexL6L12 = threading.Lock()
mutexL3L13 = threading.Lock()
mutexL7L14 = threading.Lock()
mutexL11L15 = threading.Lock()

#criação / inicalização das semaforos
sem1 = threading.Semaphore(2) #primeiro conjunto de trilhos (L2, L7 e 13)
sem2 = threading.Semaphore(2) #segundo conjunto de trilhos (L6, L11 e L14)

#variaveis que representam os trilhos laterais de cada trem
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0
l8 = 0
l9 = 0
l10 =0
l11 =0
l12 =0
l13 =0
l14 =0
l15 =0
l16 =0
l17 =0
l18 =0

#variaveis que controlam a velocidade dos trens
velocidadeTremVerde = 1
velocidadeTremLavanda = 1
velocidadeTremLaranja = 1
velocidadeTremAzul = 1

window = Tk()
window.title("Visualização Trens")
canvas = Canvas(window, width=400, height=400)
canvas.pack()

#criação das threads
t1 = threading.Thread(target=visualizarPosicaoDosTrens, args=[window] )
t2 = threading.Thread(target=trilhoVerde, args=[window, canvas] )
t3 = threading.Thread(target=trilhoLavanda, args=[window, canvas] )
t4 = threading.Thread(target=trilhoLaranja, args=[window, canvas] )
t5 = threading.Thread(target=trilhoAzul, args=[window, canvas] )
t6 = threading.Thread(target=comunicacaoComCliente, args=[])

while 1:
    if(i==0):
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        i=i+1 
    window.mainloop()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

serverSocket.close() #finaliza a conexão com o socket