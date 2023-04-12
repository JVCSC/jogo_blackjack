import random
from tkinter import *

baralho = [('Ás', 'copas'), ('2', 'copas'), ('3', 'copas'), ('4', 'copas'), ('5', 'copas'), ('6', 'copas'), ('7', 'copas'), ('8', 'copas'), ('9', 'copas'), ('10', 'copas'), ('Valete', 'copas'), ('Rainha', 'copas'), ('Rei', 'copas'), ('Ás', 'espadas'), ('2', 'espadas'), ('3', 'espadas'), ('4', 'espadas'), ('5', 'espadas'), ('6', 'espadas'), ('7', 'espadas'), ('8', 'espadas'), ('9', 'espadas'), ('10', 'espadas'), ('Valete', 'espadas'), ('Rainha', 'espadas'), ('Rei', 'espadas'), ('Ás', 'ouros'), ('2', 'ouros'), ('3', 'ouros'), ('4', 'ouros'), ('5', 'ouros'), ('6', 'ouros'), ('7', 'ouros'), ('8', 'ouros'), ('9', 'ouros'), ('10', 'ouros'), ('Valete', 'ouros'), ('Rainha', 'ouros'), ('Rei', 'ouros'), ('Ás', 'paus'), ('2', 'paus'), ('3', 'paus'), ('4', 'paus'), ('5', 'paus'), ('6', 'paus'), ('7', 'paus'), ('8', 'paus'), ('9', 'paus'), ('10', 'paus'), ('Valete', 'paus'), ('Rainha', 'paus'), ('Rei', 'paus')]
valores = {'Ás': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 10, 'Rainha': 10, 'Rei': 10}

random.shuffle(baralho)

saldo = 100

def valor_da_mao(mao):
    valor = 0
    tem_as = False
    for carta in mao:
        valor += valores[carta[0]]
        if carta[0] == 'Ás':
            tem_as = True
    if tem_as and valor <= 11:
        valor += 10
    return valor

def mostrar_mao(mao):
    for carta in mao:
        print(carta[0], 'de', carta[1])

def jogo():
    # Embaralha
    random.shuffle(baralho)

    # Cria as mãos do jogador e do dealer
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]

    # Mostra a mão do jogador e uma carta do dealer
    print('Sua mão é:')
    mostrar_mao(mao_jogador)
    print('A carta aberta do dealer é:')
    mostrar_mao([mao_dealer[0]])

    # Verifica se o jogador já tem 21
    if valor_da_mao(mao_jogador) == 21:
        print('Você tem 21!')
        return

    # Loop para as jogadas do jogador
    while True:
        escolha = input('Digite 1 para pedir carta, 2 para parar: ')
        if escolha == '1':
            mao_jogador.append(baralho.pop())
            print('Sua mão é agora:')
            mostrar_mao(mao_jogador)
            if valor_da_mao(mao_jogador) > 21:
                print('Você estourou!')
                return
        elif escolha == '2':
            break

    # Loop para as jogadas do dealer
    while valor_da_mao(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
    print('A mão do dealer é:')
    mostrar_mao(mao_dealer)

    # Verifica o vencedor
    valor_jogador = valor_da_mao(mao_jogador)
    valor_dealer = valor_da_mao(mao_dealer)
    if valor_jogador > 21:
        print('Você perdeu!')
    elif valor_dealer > 21:
        print('Você ganhou!')
    elif valor_jogador > valor_dealer:
        print('Você ganhou!')
    elif valor_dealer > valor_jogador:
        print('Você perdeu!')
    else:
        print('Empate!')

def jogar_blackjack():
    while True:
        jogo()
        resposta = input('Jogar a próxima mão? (S/N): '.upper())
        while resposta not in ['S', 'N']:
            resposta = input('Por favor, escolha entre "S" para sim e "N" para não: '.upper())
        if resposta == 'S':
            continue
        elif resposta == 'N':
            return False
    

jogar_blackjack()