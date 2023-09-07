import sys

respostas_questoes = []
respostas_corretas = []
respostas_incorretas = []


nome = input("Digite seu nome: ")
print("Seja bem-vindo", nome)

print("==== QUIZ ====")
print("Responda com a numeração de cada resposta")

resposta1 = ""
while True:
    print("\n\nA- De quem é a famosa frase 'Penso logo existo'? ")
    print("1- Platão")
    print("2- Galileu Galilei")
    print("3- Descartes")
    print("4- Sócrates")
    print("5- Francis Bacon")
    resposta1 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta1)
    
    if resposta1 == 1:
        print("Sua resposta foi: Platão")
        respostas_incorretas.append(resposta1)
        break
    elif resposta1 == 2:
        print("Sua resposta foi: Galileu Galilei")
        respostas_incorretas.append(resposta1)
        break
    elif resposta1 == 3:
        print("Sua resposta foi: Descartes")
        respostas_corretas.append(resposta1)
        break
    elif resposta1 == 4:
        print("Sua resposta foi: Sócrates")
        respostas_incorretas.append(resposta1)
        break
    elif resposta1 == 5:
        print("Sua resposta foi: Francis Bacon")
        respostas_incorretas.append(resposta1)
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta2 = ""
while True:
    print("\n\nB- De onde é a invenção do chuveiro elétrico?")
    print("1- França")
    print("2- Inglaterra")
    print("3- Brasil")
    print("4- Austrália")
    print("5- Itália")
    resposta2 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta2)

    if resposta2 == 1:
        print("Sua resposta foi: França")
        respostas_incorretas.append(resposta2)
        break
    elif resposta2 == 2:
        print("Sua resposta foi: Inglaterra")
        respostas_incorretas.append(resposta2)
        break
    elif resposta2 == 3:
        print("Sua resposta foi: Brasil")
        respostas_corretas.append(resposta2)
        break
    elif resposta2 == 4:
        print("Sua resposta foi: Austrália")
        respostas_incorretas.append(resposta2)
        break
    elif resposta2 == 5:
        print("Sua resposta foi: Itália")
        respostas_incorretas.append(resposta2)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta3 = ""
while True:
    print("\n\nC- Qual o menor país do mundo?")
    print("1- Vaticano e Rússia")
    print("2- Nauru e China")
    print("3- Mônaco e Canadá")
    print("4- Malta e Estados Unidos")
    print("5- São Mariano e Índia")
    resposta3 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta3)

    if resposta3 == 1:
        print("Sua resposta foi: Vaticano e Rússia")
        respostas_corretas.append(resposta3)
        break
    elif resposta3 == 2:
        print("Sua resposta foi: Nauru e China")
        respostas_incorretas.append(resposta3)
        break
    elif resposta3 == 3:
        print("Sua resposta foi: Mônaco e Canadá")
        respostas_incorretas.append(resposta3)
        break
    elif resposta3 == 4:
        print("Sua resposta foi: Malta e Estados Unidos")
        respostas_incorretas.append(resposta3)
        break
    elif resposta3 == 5:
        print("Sua resposta foi: São Mariano e Índia")
        respostas_incorretas.append(resposta3)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta4 = ""
while True:
    print("\n\nD- Qual o nome do presidente do Brasil que ficou conhecido como Jango?")
    print("1- Jânio Quadros")
    print("2- Jacinto Anjos")
    print("3- Getúlio Vargas")
    print("4- João Figueiredo")
    print("5- João Goulart")
    resposta4 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta4)

    if resposta4 == 1:
        print("Sua resposta foi: Jânio Quadros")
        respostas_incorretas.append(resposta4)
        break
    elif resposta4 == 2:
        print("Sua resposta foi: Jacinto Anjos")
        respostas_incorretas.append(resposta4)
        break
    elif resposta4 == 3:
        print("Sua resposta foi: Getúlio Vargas")
        respostas_incorretas.append(resposta4)
        break
    elif resposta4 == 4:
        print("Sua resposta foi: João Figueiredo")
        respostas_incorretas.append(resposta4)
        break
    elif resposta4 == 5:
        print("Sua resposta foi: João Goulart")
        respostas_corretas.append(resposta4)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta5 = ""
while True:
    print("\n\nE- Qual o livro mais vendido no mundo a seguir à Biblia?")
    print("1- O Senhor dos Anéis")
    print("2- Dom Quixote")
    print("3- O Pequeno Principe")
    print("4- Ela, a Feiticeira")
    print("5- Um Conto de Duas Cidades")
    resposta5 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta5)

    if resposta5 == 1:
        print("Sua resposta foi: O Senhor dos Anéis")
        respostas_incorretas.append(resposta5)
        break
    elif resposta5 == 2:
        print("Sua resposta foi: Dom Quixote")
        respostas_corretas.append(resposta5)
        break
    elif resposta5 == 3:
        print("Sua resposta foi: O Pequeno Princípe")
        respostas_incorretas.append(resposta5)
        break
    elif resposta5 == 4:
        print("Sua resposta foi: Ela, a Feiticeira")
        respostas_incorretas.append(resposta5)
        break
    elif resposta5 == 5:
        print("Sua resposta foi: Um Conto de Duas Cidades")
        respostas_incorretas.append(resposta5)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta6 = ""
while True:
    print("\n\nF- Quais os países que têm a maior e a menor expectativa de vida do mundo?")
    print("1- Japão e Serra Leoa")
    print("2- Austrália e Afeganistão")
    print("3- Itália e Chade")
    print("4- Brasil e Congo")
    print("5- Estados Unidos e Angola")
    resposta6 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta6)

    if resposta6 == 1:
        print("Sua resposta foi: Japão e Serra Leoa")
        respostas_corretas.append(resposta6)
        break
    elif resposta6 == 2:
        print("Sua resposta foi: Austrália e Afeganistão")
        respostas_incorretas.append(resposta6)
        break
    elif resposta6 == 3:
        print("Sua resposta foi: Itália e Chade")
        respostas_incorretas.append(resposta6)
        break
    elif resposta6 == 4:
        print("Sua resposta foi: Brasil e Congo")
        respostas_incorretas.append(resposta6)
        break
    elif resposta6 == 5:
        print("Sua resposta foi: Estados Unidos e Angola")
        respostas_incorretas.append(resposta6)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta7 = ""
while True:
    print("\n\nG- Quais as duas datas que são comemoradas em novembro?")
    print("1- Independência do Brasil e Dia da Bandeira")
    print("2- Proclamação da República e Dia Nacional da Consciência Negra")
    print("3- Dia do Médico e Dia de São Lucas")
    print("4- Dia de Finados e Dia Nacional do Livro")
    print("5- Black Friday e Dia da Árvore")
    resposta7 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta7)

    if resposta7 == 1:
        print("Sua resposta foi: Independência do Brasil e Dia da Bandeira")
        respostas_incorretas.append(resposta7)
        break
    elif resposta7 == 2:
        print("Sua resposta foi: Proclamação da República e Dia Nacional da Consciência Negra")
        respostas_corretas.append(resposta7)
        break
    elif resposta7 == 3:
        print("Sua resposta foi: Dia do Médico e Dia de São Lucas")
        respostas_incorretas.append(resposta7)
        break
    elif resposta7 == 4:
        print("Sua resposta foi: Dia de Finados e Dia Nacional do Livro")
        respostas_incorretas.append(resposta7)
        break
    elif resposta7 == 5:
        print("Sua resposta foi: Black Friday e Dia da Árvore")
        respostas_incorretas.append(resposta7)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

reposta8 = ""
while True:
    print("\n\nH- Quanto tempo a luz do Sol demora para chegar à Terra?")
    print("1- 12 minutos")
    print("2- 1 dia")
    print("3- 12 horas")
    print("4- 8 minutos")
    print("5- 12 segundos")
    resposta8 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta8)

    if resposta8 == 1:
        print("Sua resposta foi: 12 minutos")
        respostas_incorretas.append(resposta7)
        break
    elif resposta8 == 2:
        print("Sua resposta foi: 1 dia")
        respostas_corretas.append(resposta7)
        break
    elif resposta8 == 3:
        print("Sua resposta foi: 12 horas")
        respostas_incorretas.append(resposta7)
        break
    elif resposta8 == 4:
        print("Sua resposta foi: 8 minutos")
        respostas_corretas.append(resposta7)
        break
    elif resposta8 == 5:
        print("Sua resposta foi: 12 segundos")
        respostas_incorretas.append(resposta7)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

resposta9 = ""
while True:
    print("\n\nJ- Qual personagem folclórico costuma ser agradado pelos caçadores com a oferta de fumo?")
    print("1- Caipora")
    print("2- Saci")
    print("3- Lobisomem")
    print("4- Boitatá")
    print("5- Negrinho do Pastoreiro")
    resposta9 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta9)

    if resposta9 == 1:
        print("Sua resposta foi: Caipora")
        respostas_corretas.append(resposta9)
        break
    elif resposta9 == 2:
        print("Sua resposta foi: Saci")
        respostas_incorretas.append(resposta9)
        break
    elif resposta9 == 3:
        print("Sua resposta foi: Lobisomem")
        respostas_incorretas.append(resposta9)
        break
    elif resposta9 == 4:
        print("Sua resposta foi: Boitatá")
        respostas_incorretas.append(resposta9)
        break
    elif resposta9 == 5:
        print("Sua resposta foi: Negrinho Pastoreiro")
        respostas_incorretas.append(resposta9)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue

reposta10 = ""
while True:
    print("\n\nH- Qual a montanha mais alta do Brasil?")
    print("1- Pico da Neblina")
    print("2- Pico Paraná")
    print("3- Monte Roraíma")
    print("4- Pico Maior de Friburgo")
    print("5- Pico da Bandeira")
    resposta10 = int(input("Digite sua alternativa: "))
    respostas_questoes.append(resposta10)

    if resposta10 == 1:
        print("Sua resposta foi: Pico da Neblina")
        respostas_corretas.append(resposta9)
        break
    elif resposta10 == 2:
        print("Sua resposta foi: Pico Paraná")
        respostas_incorretas.append(resposta9)
        break
    elif resposta10 == 3:
        print("Sua resposta foi: Monte Raraíma")
        respostas_incorretas.append(resposta9)
        break
    elif resposta10 == 4:
        print("Sua resposta foi: Pico Maior de Friburgo")
        respostas_incorretas.append(resposta9)
        break
    elif resposta10 == 5:
        print("Sua resposta foi: Pico da Bandeira")
        respostas_incorretas.append(resposta9)
        break
    else:
        print("\n\nResposta Incorreta!\n\n")
        input("Pressione ENTER para continuar")
        continue


print("\n\nSuas respostas foram: ", respostas_questoes)
print("\n\nRespostas corretas foram: ", len(respostas_corretas))
print("\n\nRespostas incorretas foram: ", len(respostas_incorretas))

print("\n\nDeseja sair do programa?: 1- sim 2- não")
close = input()

if close == 1:
    print("Saindo do programa...")
    sys.exit(0)