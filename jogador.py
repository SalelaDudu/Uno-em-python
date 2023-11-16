class Player:
    mao = []    
    
    def __init__(self,mao):
        self.mao = mao

    def uno(self):
        if len(mao) == 1:
            print('Você está de Uno')
        
    def jogada(self,carta, monte):        
        indice = len(monte) - 1
        ultima_carta = monte[i]
        if carta.coringa == True:
            if carta.numero == '+4':
                computador.comprar(4)
                ultima_carta.cor =  input('selecione uma cor:')
            else:
                ultima_carta.cor =  input('selecione uma cor:')            
        elif carta.numero == ultima_carta.numero or carta.cor == ultima_carta.cor:
            monte.append(carta)
            self.mao.pop(carta)
            print("você jogou " + carta)
        else:
            print('error')
                
    def jogar(self,carta):
        if carta in mao:
            monte.append(carta)
            self.mao.remove(carta)
            print("Você jogou: "+ carta)
        else:
            print("Jogue uma carta!")
            
    def comprar(self,i,baralho):
        for n in range(i):
            self.mao.append(baralho[0])
            baralho.pop(0)            

    def ver_cartas(self):
        mao = self.mao
        for i in mao:
            print(i.numero, i.cor)

class Computador:
       mao = []    
    
    def __init__(self,mao):
        self.mao = mao

    def uno(self):
        if len(mao) == 1:
            print('Computador está de Uno')
        
    def jogada(self,carta, monte):        
        indice = len(monte) - 1
        ultima_carta = monte[i]
        if carta.coringa == True:
            if carta.numero == '+4':
                computador.comprar(4)
                ultima_carta.cor =  input('selecione uma cor:')
            else:
                ultima_carta.cor =  input('selecione uma cor:')
        elif carta.numero == ultima_carta.numero or carta.cor == ultima_carta.cor:
            monte.append(carta)
            self.mao.pop(carta)
            print("você jogou " + carta)
        else:
            print('error')
                
    def jogar(self,carta):
        if carta in mao:
            monte.append(carta)
            self.mao.remove(carta)
            print("Você jogou: "+ carta)
        else:
            print("Jogue uma carta!")
            
    def comprar(self,i,baralho):
        for n in range(i):
            self.mao.append(baralho[0])
            baralho.pop(0)            

    def ver_cartas(self):
        mao = self.mao
        for i in mao:
            print(i.numero, i.cor)