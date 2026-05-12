from colorama import Fore, Style

print ('=================================\n'
f'{Fore.GREEN}{Style.BRIGHT}Boas vindas ao Jobóia Rasp Quiz!\n'
f'{Style.RESET_ALL}'
'=================================\n\n'
'=================================================================\n'
f'{Fore.WHITE}Jobóia Rasp Quiz é um jogo educativo infantil;\n'
f'Seu objetivo é despertar o interesse por tecnologia;\n'
f'É um jogo que funciona em modo texto;\n'
f'Foi criado com a linguagem de programação Python;\n'
f'E combina programação (Software) com Hardware(Protoboard e LEDs);\n'
f'Tudo o que você faz no jogo gera respostas físicas;\n'
f'Você vai ouvir sons de BIP e luzes piscando!\n'
f'Aprenda tecnologia de forma divertida e interativa!{Style.RESET_ALL}\n'
f'=================================================================')

while True:
    print(f'{Fore.GREEN}{Style.BRIGHT}\nRegras do jogo:{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Serão feitas 10 perguntas;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Cada pergunta possui apenas uma resposta certa;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Cada resposta certa vale 10 pontos;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Você deverá responder as perguntas digitando uma das letras (a, b, c ou d);{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Em caso de resposta >certa< o led verde vai piscar e serão tocados vários sons de bip;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Em caso de resposta >errada< o led vermelho vai piscar e será tocado um longo som de bip;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Respostas certas valem 10 pontos;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Respostas erradas valem 0 pontos;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}O jogo irá calcular sua média no final;{Style.RESET_ALL}\n'
    f'{Fore.GREEN}{Style.BRIGHT}->{Style.RESET_ALL} {Fore.WHITE}Divirta-se!{Style.RESET_ALL}\n')

    points = 0
    ask1 = input (f'{Fore.WHITE}{Style.BRIGHT}1. Qual é o nome do rio que passa pela cidade de São Paulo?{Style.RESET_ALL}\n' 
    'A) Rio Amazonas\n'
    'B) Rio Tietê\n'
    'C) Rio Paraná\n'
    'D) Rio da Prata\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask1:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask2 = input (f'{Fore.WHITE}{Style.BRIGHT}2. Qual destes animais é muito comum de ver em parques de São Paulo?{Style.RESET_ALL}\n'
    'A) Capivara\n'
    'B) Camelo\n'
    'C) Pinguim\n'
    'D) Lobo-Guará\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask2:
        case 'A':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
           print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask3 = input (f'{Fore.WHITE}{Style.BRIGHT}3. Em qual estado fica a cidade de São Paulo?{Style.RESET_ALL}\n'
    'A) Rio de Janeiro\n'
    'B) Bahia\n'
    'C) São Paulo\n'
    'D) Minas Gerais\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask3:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask4 = input (f'{Fore.WHITE}{Style.BRIGHT}4. Qual destes meios de transporte existe em São Paulo?{Style.RESET_ALL}\n'
    'A) Metrô\n'
    'B) Trenó\n'
    'C) Navio pirata\n'
    'D) Nave espacial\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask4:
        case 'A':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'B': 
             print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask5 = input (f'{Fore.WHITE}{Style.BRIGHT}5. Qual é a cor principal da bandeira do estado de São Paulo?{Style.RESET_ALL}\n'
    'A) Azul\n'
    'B) Preto e branco\n'
    'C) Verde\n'
    'D) Rosa\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask5:
        case 'A':
            print ('>>Errado<<\n')
        case 'B':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask6 = input (f'{Fore.WHITE}{Style.BRIGHT}6. O que devemos fazer antes de atravessar a rua?{Style.RESET_ALL}\n'
    'A) Correr sem olhar\n'
    'B) Fechar os olhos\n'
    'C) Olhar para os dois lados\n'
    'D) Andar pelo meio dos carros\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask6:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')


    ask7 = input (f'{Fore.WHITE}{Style.BRIGHT}7. Qual destes alimentos é considerado saudável{Style.RESET_ALL}\n'
    'A) Pizza\n'
    'B) Batata frita\n'
    'C) Hamburguer\n'
    'D) Maçã\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask7:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask8 = input(f'{Fore.WHITE}{Style.BRIGHT}8. Em qual lugar as crianças vão estudar?{Style.RESET_ALL}\n'
    'A) Cinema\n'
    'B) Escola\n'
    'C) Shopping\n'
    'D) Praia\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask8:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask9 = input (f'{Fore.WHITE}{Style.BRIGHT}9. Qual destes é um ponto famoso da cidade de São Paulo?{Style.RESET_ALL}\n'
    'A) Torre Eiffel\n'
    'B) Coliseu\n'
    'C) Avenida Paulista\n'
    'D) Elvador Lacerda\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask9:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case 'D':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    ask10 = input (f'{Fore.WHITE}{Style.BRIGHT}10. Qual desses itens é uma peça de computador?{Style.RESET_ALL}\n'
    'A) Jaca\n'
    'B) Mochila\n'
    'C) Sapato\n'
    'D) Teclado\n\n'
    'Digite a letra da resposta certa: ').upper()

    match ask10:
        case 'A':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'B':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print (f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'D':
            print (f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
        case _:
            print (f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')

    print(f'=================================================================\nA sua pontuação final foi de: {points} pontos de um total de 100 pontos\n=================================================================\n')

    play_again = input ('E aí! Quer jogar de novo? Digite >S< para sim e >N< para não:\n').upper()
    if play_again != 'S':
        print ('Obrigado por jogar! Até mais!\n')
        break