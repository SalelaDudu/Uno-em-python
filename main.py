from baralho import *
import jogador

jogadores = []
monte = []
mao_jogador = []
mao_computador = []
turno = []

baralho = init_baralho()
embaralhar(baralho)

computador = jogador.Computador(mao_computador)
jogador = jogador.Player(mao_jogador)

jogadores = [jogador,computador]
for i in jogadores:
    turno.append(i)

print('[1] Jogador primeiro','\n[2] Computador primeiro','\n[3] Aleatório')
turn_order = input("Escolha a ordem de turno: " or 1)

if turn_order == '2':
    turno.reverse()    
elif turn_order == '3':
    for i in range(10):
        random.shuffle(turno)

monte.append(baralho[-1])
baralho.pop()

carta_atual = monte[-1]

jogador.comprar(7,baralho)
computador.comprar(7,baralho)

while True:
    for i in turno:
        carta_atual = monte[-1]
        print("A carta do monte é: ",carta_atual.numero,carta_atual.cor)
        if i.__class__.__name__ == 'Player':
            tam = len(monte)
            while True:
                jogador.uno()
                jogador.acoes(monte)
                if len(monte) > tam:
                    break
            
        if i.__class__.__name__ == 'Computador':
            print("hab")
    break            