palavraSecreta = raw_input('Digite a palavra secreta: ').lower().strip()#.lower(Deixa todas as letras em minusculo p/ que nao haja problemas)
                                                                   #.strip(Elimina todos os espacos antes e depois da palavra secreta)
for x in range(200):                                            
     print('|:D| '* 20)          #Faz a palavra secreta 'sumir'

digitadas = []
correto = []
incorreto = 0

while True:
     secreta = ''
     for letra in palavraSecreta: 
         if (letra in correto):
             secreta += letra
         else:
             secreta += '-'
     print('\nA palavra secreta é {}.'.format(secreta))
     
     if secreta == palavraSecreta:
         print('Você acertou!')
         break
         
     tentativa = raw_input('\nDigite uma letra: ').lower().strip()
     print('')
     if tentativa in digitadas:
         print('ATENCAO \nVocê já digitou a letra "{}"!\n'.format(tentativa))
         continue
     else:
         digitadas += tentativa
         if tentativa in palavraSecreta:
               correto += tentativa
               print('Correto \nA letra "{}" PERTENCE a palavra!\n'.format(tentativa))
         else:
               incorreto += 1
               print('Incorreto \nA letra "{}" NAO PERTENCE a palavra!\n'.format(tentativa))
     print(' ____ ___\n |   |   ')
     print(' | (*.*) ' if incorreto >= 1 else ' |')
     linha2 = ''
     if incorreto == 2:
         linha2 = '   |   '
     elif incorreto == 3:
         linha2 = ' *\|   '
     elif incorreto >= 4:
         linha2 = ' *\|/* '
     print(' |{}'.format(linha2))
     linha3 = ''
     if incorreto == 5:
         linha3 += ' _/     '
     elif incorreto >= 6:
         linha3 += ' _/ \_ '
     print (' |{}'.format(linha3))
     print(' |\n________________')
     if incorreto == 6:
         print("Voce foi enforcado!\nO jogo acabou!!!")
         break
