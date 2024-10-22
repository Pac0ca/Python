###Questão 02: Faça um algoritmo em Python que leia um número indeterminado de notas. Após as entradas de dados, faça o seguinte:
##• Mostre a quantidade de notas que foram lidas.
##• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
##• Calcule e mostre a média das notas.
##• Mostre as notas acima da média calculada
notas = 0
notasl = []

while notas != -1:
    notas = float(input("Adicione as notas ou -1 para terminar: "))
    if notas!= -1:
        notasl.append(notas)
print('A quantidades de valores lidos foram:', len(notasl))
print('<>'*40)
notasl.reverse()
print(notasl)
soma = sum(notasl)
quant= len(notasl)
media= soma/quant
print('<>'*40)
print(f'A média das notas é:{media}')
print('<>'*40)
mmedias = []
for notas in notasl:
   if notas > media:
      mmedias = notas
      print(f"As notas maiores que a medias são: {mmedias}")
      print('<>'*40)

    
        
    
    
