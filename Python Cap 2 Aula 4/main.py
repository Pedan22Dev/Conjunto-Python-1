tabuada = int(input('Digite um numero para exibir a tabuada: '))
print('A tabuada do numero', tabuada)
for valor in range(0, 11, 1):
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada*valor)))


print('Fim de transmissão') 
