nome =  input('Digite seu nome: ')
idade =  int(input('digite a sua idade: '))
doenca_infectocontagiosa = input("Suspeita de doença contagiosa? ").upper()


if idade >= 65:
    print("O paciente " + nome + " requer atendimento prioritário")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada")
else:
    print("O paciente " + nome + " não requer atendimento prioritário, e pode aguardar na sala comum.")
print('Fim de transmissão') 
