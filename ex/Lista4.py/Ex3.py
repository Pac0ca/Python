###Seu amigo Gabriel está precisando de um favor. Está lhe pedindo um algoritmo Python que ajude a controlar os gastos mensais de suas contas de energias.
###Para cada conta de luz que Gabriel recebe na caixa dos correios, cadastra-se: data em que a leitura do relógio de luz foi realizada, mês correspondente, valor atual do relógio do contador, quantidade de Kw gasto no mês, valor a pagar pela conta, data do vencimento e média de consumo.

###Para facilitar o controle de Gabriel, seu algoritmo dele permitir que ele realize as seguintes pesquisas:

##- verificação do mês de menor consumo.
##- verificação do mês de maior consumo.

conta = {}
final = 's'
ma=0
me = 99999999
while final != 'n':
    
    conta['data'] = int(input( 'Informe data em que ouve a leitura do relógio de luz: '))
    conta['mes'] = int(input( 'Informe o mês correspondente: '))
    conta['valor_r'] = float(input( 'Informe o valor atual do relógio do contador: ')) 
    conta['kw'] = float(input( 'Informe a quantidade de Kw gasto no mês: ')) 
    conta['valor'] = float(input( 'Informe o valor a pagar pela conta: ')) 
    conta['data_v'] = int(input( 'Informe a data de vancimento: ')) 
    conta['media'] = int(input( 'Informe a média de comsumo: ')) 
    if me == 99999999:
        me = conta['valor']
    else:
        if conta['valor'] > ma:
            ma = conta['valor']
        elif conta['valor'] < me:
            me = conta['valor']
    
           
    print("x"*40)
    final = input('Deseja cuntinuar? \nS/N: ')
    
print(f'O maior mes de consumo é: {ma}')
print(f'O menor mes de consumo é: {me}')

 

