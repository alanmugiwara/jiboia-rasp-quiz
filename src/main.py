from gpiozero import PWMOutputDevice, LED
from gpiozero.tones import Tone
from time import sleep
from colorama import Fore, Style

# Variáveis de controle de LED GPIO (todos 3.3v)
led_green = LED(17)
led_yellow = LED(27)
led_red = LED(22)

# Variável de controle Buzzer GPIO (3.3v)
buzzer_song = PWMOutputDevice(21)

name = ''

# Função p/ resposta certa: acende o LED verde e toca vários bips rápidos
def resp_certa():
    led_green.on()

    # vários bips rápidos
    for i in range(3):
        buzzer_song.on()
        sleep(0.2)
        buzzer_song.off()
        sleep(0.2)

    sleep(0.5)
    led_green.off()

# Função p/ resposta errada: acende o LED vermelho e toca um bip longo
def resp_errada():
    led_red.on()
    # bip longo
    buzzer_song.on()
    sleep(1)
    buzzer_song.off()

    led_red.off()

# Função p/ resposta inválida: acende o LED amarelo e toca dois bips rápidos
def resp_invalida():
    led_yellow.on()

    # dois bips rápidos
    for i in range(2):
        buzzer_song.on()
        sleep(0.1)
        buzzer_song.off()
        sleep(0.1)

    sleep(0.5)
    led_yellow.off()

def ending_song():
    volume = 0.8
    mario_music = [
        ('E5', 0.15), (None, 0.05),
        ('E5', 0.15), (None, 0.15),
        ('E5', 0.15), (None, 0.15),
        ('C5', 0.15), ('E5', 0.30),
        ('G5', 0.30), (None, 0.30),
        ('G4', 0.30), (None, 0.30),
        ('C5', 0.30), (None, 0.15),
        ('G4', 0.30), (None, 0.15),
        ('E4', 0.30), (None, 0.15),
        ('A4', 0.30), ('B4', 0.30),
        ('Bb4', 0.15), ('A4', 0.30),
        ('G4', 0.20), ('E5', 0.20), ('G5', 0.20),
        ('A5', 0.30), ('F5', 0.15), ('G5', 0.15),
        (None, 0.15), ('E5', 0.30),
        ('C5', 0.15), ('D5', 0.15), ('B4', 0.30),
        (None, 0.30),
        ('C5', 0.30), (None, 0.15),
        ('G4', 0.30), (None, 0.15),
        ('E4', 0.30), (None, 0.15),
        ('A4', 0.30), ('B4', 0.30),
        ('Bb4', 0.15), ('A4', 0.30),
        ('G4', 0.20), ('E5', 0.20), ('G5', 0.20),
        ('A5', 0.30), ('F5', 0.15), ('G5', 0.15),
        (None, 0.15), ('E5', 0.30),
        ('C5', 0.15), ('D5', 0.15), ('B4', 0.30),
        (None, 0.30)
        ]

    for notas, duracao in mario_music:
        if notas is None:
            # É uma pausa, zera o volume
            buzzer_song.value = 0
            sleep(duracao)
        else:
            # É uma nota, toca na frequência correta            
            buzzer_song.frequency = Tone(notas).frequency
            buzzer_song.value = volume
            sleep(duracao)
            
            # Silêncio ráido pras notas não se grudarem
            buzzer_song.value = 0
            sleep(0.01)

    # Desliga tudo
    buzzer_song.value = 0
    buzzer_song.off()

print('=================================\n'
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

name = input ('\nAntes de começar o jogo. Qual o seu nome? ')

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
    ask1 = input(f'{Fore.WHITE}{Style.BRIGHT}1. Qual é o nome do rio que passa pela cidade de São Paulo?{Style.RESET_ALL}\n'
        'A) Rio Amazonas\n'
        'B) Rio Tietê\n'
        'C) Rio Paraná\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask1:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(
                f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask2 = input(f'{Fore.WHITE}{Style.BRIGHT}2. Qual destes animais é muito comum de ver em parques de São Paulo?{Style.RESET_ALL}\n'
        'A) Capivara\n'
        'B) Camelo\n'
        'C) Pinguim\n'
        'D) Lobo-Guará\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask2:
        case 'A':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(
                f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask3 = input(f'{Fore.WHITE}{Style.BRIGHT}3. Em qual estado fica a cidade de São Paulo?{Style.RESET_ALL}\n'
        'A) Rio de Janeiro\n'
        'B) Bahia\n'
        'C) São Paulo\n'
        'D) Minas Gerais\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask3:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask4 = input(f'{Fore.WHITE}{Style.BRIGHT}4. Qual destes meios de transporte existe em São Paulo?{Style.RESET_ALL}\n'
        'A) Metrô\n'
        'B) Trenó\n'
        'C) Navio pirata\n'
        'D) Nave espacial\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask4:
        case 'A':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask5 = input(
        f'{Fore.WHITE}{Style.BRIGHT}5. Qual é a cor principal da bandeira do estado de São Paulo?{Style.RESET_ALL}\n'
        'A) Azul\n'
        'B) Preto e branco\n'
        'C) Verde\n'
        'D) Rosa\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask5:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask6 = input(
        f'{Fore.WHITE}{Style.BRIGHT}6. O que devemos fazer antes de atravessar a rua?{Style.RESET_ALL}\n'
        'A) Correr sem olhar\n'
        'B) Fechar os olhos\n'
        'C) Olhar para os dois lados\n'
        'D) Andar pelo meio dos carros\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask6:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask7 = input(
        f'{Fore.WHITE}{Style.BRIGHT}7. Qual destes alimentos é considerado saudável{Style.RESET_ALL}\n'
        'A) Pizza\n'
        'B) Batata frita\n'
        'C) Hamburguer\n'
        'D) Maçã\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask7:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask8 = input(
        f'{Fore.WHITE}{Style.BRIGHT}8. Em qual lugar as crianças vão estudar?{Style.RESET_ALL}\n'
        'A) Cinema\n'
        'B) Escola\n'
        'C) Shopping\n'
        'D) Praia\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask8:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask9 = input(
        f'{Fore.WHITE}{Style.BRIGHT}9. Qual destes é um ponto famoso da cidade de São Paulo?{Style.RESET_ALL}\n'
        'A) Torre Eiffel\n'
        'B) Coliseu\n'
        'C) Avenida Paulista\n'
        'D) Elevador Lacerda\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask9:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case 'D':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    ask10 = input(
        f'{Fore.WHITE}{Style.BRIGHT}10. Qual desses itens é uma peça de computador?{Style.RESET_ALL}\n'
        'A) Jaca\n'
        'B) Mochila\n'
        'C) Sapato\n'
        'D) Teclado\n\n'
        f'Digite a letra da resposta certa e aperte {Fore.WHITE}{Style.BRIGHT}>ENTER<:{Style.RESET_ALL} ').upper()

    match ask10:
        case 'A':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'B':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'C':
            print(f'{Fore.RED}{Style.BRIGHT}>>Errado!<<{Style.RESET_ALL}\n')
            resp_errada()
        case 'D':
            print(f'{Fore.GREEN}{Style.BRIGHT}>>Certo!<<{Style.RESET_ALL}\n')
            points += 10
            resp_certa()
        case _:
            print(f'{Fore.YELLOW}{Style.BRIGHT}>>Resposta inválida<<{Style.RESET_ALL}\n')
            resp_invalida()

    print(
        f'{Fore.CYAN}{Style.BRIGHT}'
        '╔════════════════════════════════════════════════════╗\n'
        '║                 RESULTADO FINAL                    ║\n'
        '╚════════════════════════════════════════════════════╝\n'
        f'{Style.RESET_ALL}'
        
        f'\n{Fore.WHITE}{Style.BRIGHT}{name}{Style.RESET_ALL}{Fore.WHITE}, a sua pontuação foi:{Style.RESET_ALL} '
        f'{Fore.GREEN}{Style.BRIGHT}{points} pontos{Style.RESET_ALL}'
        f'{Fore.CYAN}{Style.BRIGHT} de um total de 100 pontos.{Style.RESET_ALL}\n')
    ending_song()

    play_again = input(f'E aí! Quer jogar de novo? Digite '
                       f'{Fore.GREEN}{Style.BRIGHT}>S<{Style.RESET_ALL} para '
                       f'{Fore.GREEN}{Style.BRIGHT}sim{Style.RESET_ALL} e '
                       f'{Fore.RED}{Style.BRIGHT}>N<{Style.RESET_ALL} para '
                       f'{Fore.RED}{Style.BRIGHT}não{Style.RESET_ALL}:\n').upper()
    if play_again != 'S':
        print('Obrigado por jogar! Até mais!\n')
        break