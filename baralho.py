import random

cartas = ['0','1','2','3','4','5','6','7','8','9','+2','bloqueio','inverte','+4','muda cor']
cores = ['azul','amarelo','vermelho','verde']

class Carta:
    numero = str
    cor = str
    coringa = bool
    def __init__(self,numero,cor,coringa):
        self.numero = numero
        self.cor = cor
        self.coringa = coringa

def init_baralho():
    baralho = []
    for i in range(4):
        for ca in cartas:
            for cor in cores:
                if ca == '+4' or ca == 'muda cor':
                    baralho.append(Carta(ca,'Null',True))
                else:
                    baralho.append(Carta(ca,cor,False))

    return baralho        

def embaralhar(baralho):
    for i in range(8):
        random.shuffle(baralho)
            
def reset_baralho(baralho,monte):
    for i in monte:
        baralho.append(i)
    embaralhar()
