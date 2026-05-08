print ('=================================\n'
'Boas vindas ao Jobóia Rasp Quiz!\n'
'=================================\n\n'
'===========================================================\n'
'É um jogo educativo infantil para despertar o interesse por tecnologia;\n'
'É um jogo que funciona totalmente via texto;\n'
'Foi criado com a linguagem de programação Python;\n'
'E combina programação com Hardware;\n'
'Tudo o que você faz no jogo gera respostas físicas;\n'
'Você vai ouvir sons de BIP e luzes piscando!\n'
'===========================================================\n')

print('Regras do jogo:\n'
'-> Serão feitas 10 perguntas;\n'
'-> Cada pergunta possui apenas uma resposta certa;\n'
'-> Cada resposta certa vale 10 pontos;\n'
'-> Você deverá responder as perguntas digitando uma das letras (a, b, c ou d);\n'
'-> Em caso de resposta >certa< o led verde vai piscar e serão tocados vários sons de bip;\n'
'-> Em caso de resposta >errada< o led vermelho vai piscar e será tocado um longo som de bip;\n'
'-> Respostas certas valem 10 pontos;\n'
'-> Respostas erradas valem 0 pontos;\n'
'-> O jogo irá calcular sua média no final;\n'
'-> Divirta-se!\n')

ask1 = input ('1. Qual é o nome do rio que passa pela cidade de São Paulo?\n' 
'A) Rio Amazonas\n'
'B) Rio Tietê\n'
'C) Rio Paraná\n'
'D) Rio da Prata\n\n'
'Digite a letra da resposta certa: ').upper()

match ask1:
    case 'A': print ('>>Errado!<<\n') 
    case 'B': print ('>>Certo!<<\n')
    case 'C': print ('>>Errado!<<\n')
    case 'D': print ('>>Errado!<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask2 = input ('2. Qual destes animais é muito comum de ver em parques de São Paulo?\n'
'A) Capivara\n'
'B) Camelo\n'
'C) Pinguim\n'
'D) Lobo-Guará\n\n'
'Digite a letra da resposta certa: ').upper()

match ask2:
    case 'A': print ('>>Certo!<<\n')
    case 'B': print ('>>Errado!<<\n')
    case 'C': print ('>>Errado!<<\n')
    case 'D': print ('>>Errado!<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask3 = input ('3. Em qual estado fica a cidade de São Paulo?\n'
'A) Rio de Janeiro\n'
'B) Bahia\n'
'C) São Paulo\n'
'D) Minas Gerais\n\n'
'Digite a letra da resposta certa: ').upper()

match ask3:
    case 'A': print ('>>Errado!<<\n')
    case 'B': print ('>>Errado!!<<\n')
    case 'C': print ('>>Certo!<<\n')
    case 'D': print ('>>Errado!<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask4 = input ('4. Qual destes meios de transporte existe em São Paulo?\n'
'A) Metrô\n'
'B) Trenó\n'
'C) Navio pirata\n'
'D) Nave espacial\n\n'
'Digite a letra da resposta certa: ').upper()

match ask4:
    case 'A': print ('>>Certo!<<\n')
    case 'B': print ('>>Errado!<<\n')
    case 'C': print ('>>Errado!<<\n')
    case 'D': print ('>>Errado!<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask5 = input ('5. Qual é a cor principal da bandeira do estado de São Paulo?\n'
'A) Azul\n'
'B) Preto e branco\n'
'C) Verde\n'
'D) Rosa\n\n'
'Digite a letra da resposta certa: ').upper()

match ask5:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Certo<<\n')
    case 'C': print ('>>Errado<<\n')
    case 'D': print ('>>Errado<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask6 = input ('6. O que devemos fazer antes de atravessar a rua?\n'
'A) Correr sem olhar\n'
'B) Fechar os olhos\n'
'C) Olhar para os dois lados\n'
'D) Andar pelo meio dos carros\n\n'
'Digite a letra da resposta certa: ').upper()

match ask6:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Errado<<\n')
    case 'C': print ('>>Certo<<\n')
    case 'D': print ('>>Errado<<\n')
    case _: print ('>>Resposta inválida<<\n')


ask7 = input ('7. Qual destes alimentos é considerado saudável\n'
'A) Pizza\n'
'B) Batata frita\n'
'C) Hamburguer\n'
'D) Maçã\n\n'
'Digite a letra da resposta certa: ').upper()

match ask7:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Errado<<\n')
    case 'C': print ('>>Errado<<\n')
    case 'D': print ('>>Certo<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask8 = input('8. Em qual lugar as crianças vão estudar?\n'
'A) Cinema\n'
'B) Escola\n'
'C) Shopping\n'
'D) Praia\n\n'
'Digite a letra da resposta certa: ').upper()

match ask8:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Certo<<\n')
    case 'C': print ('>>Errado<<\n')
    case 'D': print ('>>Errado<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask9 = input ('9. Qual destes é um ponto famoso da cidade de São Paulo?\n'
'A) Torre Eiffel\n'
'B) Coliseu\n'
'C) Avenida Paulista\n'
'D) Elvador Lacerda\n\n'
'Digite a letra da resposta certa: ').upper()

match ask9:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Errado<<\n')
    case 'C': print ('>>Certo<<\n')
    case 'D': print ('>>Errado<<\n')
    case _: print ('>>Resposta inválida<<\n')

ask10 = input ('10. Qual desses itens é uma peça de computador?\n'
'A) Jaca\n'
'B) Mochila\n'
'C) Sapato\n'
'D) Teclado\n\n'
'Digite a letra da resposta certa: ').upper()

match ask10:
    case 'A': print ('>>Errado<<\n')
    case 'B': print ('>>Errado<<\n')
    case 'C': print ('>>Errado<<\n')
    case 'D': print ('>>Certo<<\n')
    case _: print ('>>Resposta inválida<<\n')