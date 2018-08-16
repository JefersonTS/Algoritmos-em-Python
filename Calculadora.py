print('\nEscolha uma das opcoes abaixo.\n')
print('A _ Calcular a tabuada de um número de 1 a 9;')
print('B _ Calcular o índice de massa corporal;')
print('C _ Calcular o fatorial de um número inteiro;')
print('D _ Descobrir o menor elemento de um vetor;')
print('E _ Obter a média dos elementos ímpares de um vetor de 20 posições.')
print('_'*70)
opc = ''
while(opc == ''):
    opc = str(raw_input('Informe sua opção: ')).lower().strip()
    print(' ')
    
    if(opc !='a' and opc !='b' and opc !='c' and opc !='d' and opc !='e'):
        print('Informe uma opção válida.\n')
        
    if(opc == 'a'):
        def calcular_tabuada(_numero):
            numero = int(_numero)
            if(numero <= 0):
                print('Informe um número inteiro entre 1 e 10.')
                
            if(numero > 10):
                print('Informe um número inteiro entre 1 e 9.')
                
            if(numero >= 1 and numero <= 10):
                for i in range(1,11):
                    print i,"*" ,numero, "=" ,i*numero
                    
        numero_escolhido = int(input('Informe o número: '))
        print(' ')
        enviar_tabuada = calcular_tabuada(numero_escolhido)
        
    if(opc == 'b'):
        def calcular_IMC(_peso,_altura):
            def_peso = float(_peso)
            def_altura = float(_altura)
            IMC = def_peso/(def_altura**def_altura)
            return IMC
        peso = float(input('Informe o seu peso: '))
        print(' ')
        
        altura = float(input('Informe a sua altura: '))
        print(' ')
        
        dados_IMC = calcular_IMC(peso, altura)
        print('O seu IMC é de {} \n'.format(dados_IMC))
        
    if(opc == 'c'):
        def calcular_fatorial(_numero):
            numero = _numero
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            return fatorial
		
        escolha_numero = int(input('Informe o número: '))
        print(' ')
        
        result = calcular_fatorial(escolha_numero)
        print('O fatorial de {} e igual a {}'.format(escolha_numero, result))
        print(' ')
        
    if(opc == 'd'):
        def menor_elemento(_vetor):
            vetor = _vetor
            menorvalor = min(vetor)
            return menorvalor
        tamanhovetor = int(input('Informe o tamanho do vetor: '))
        print(' ')
        vetor1 = []
        for i in range(0, tamanhovetor):
            vetor1.append(float(input('Informe o valor da {} posição do vetor: ' .format(i+1) )))
        resultado = menor_elemento(vetor1)
        print(' ')
        print('O menor elemento do vetor é {} \n'.format(int(resultado)))
        
    if(opc == 'e'):
        def media_impar(total_impar, quantidade_impar):
            
            totalimpar = total_impar
            quantidadeimpar = quantidade_impar
            mediaimpar = totalimpar/quantidadeimpar
            return mediaimpar
					
        vet = []
        totimpar = 0
        qtdimpar = 0
        for i in range(0,20):
            vet.append(int(input('Informe o valor da {} posição: '.format(i+1))))
        for i in range(0, 20):
            if(vet[i] % 2 == 1):
                totimpar += vet[i]
                qtdimpar += 1
        print(' ')
        media = media_impar(totimpar, qtdimpar)
        print('A média dos elementos ímpares do vetor é de',media)
        break	
