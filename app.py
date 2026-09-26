quantidade_excelente=0
quantidade_ruim=0

for i in range(50):
    print ("estrevistados: ", i+1)
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))

    print("Menu de Avalição: ")
    print("1-Excelente")
    print("2-Bom")
    print("3-Ruim")
    opiniao=int(input("Sua opinião é muito importante para a TudoWeb! Digite sua nota (1,2 ou 3): "))
    while opiniao < 1 or opiniao >3:
        print("Opinião inválida! Escolha apenas 1,2 ou 3.")
        opiniao=int(input("Sua opinião é muito importante para a TudoWeb! Digite sua nota (1,2 ou 3): "))

    if opiniao ==1:
            quantidade_excelente +=1
    elif opiniao ==3:
            quantidade_ruim +=1
 
print("RESULTADO DA PESQUISA")
print("Quantidade de respostas 'Excelente':", quantidade_excelente)
print("Quantidade de respostas 'Ruim':", quantidade_ruim)

