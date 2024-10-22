###Dicionario de um produto
produto1 = {
    'codigo': 1,
    'descrição': 'Arroz Preto',
    'Quantidade': 35,
    'Valor': 5.60
}

#print(produto)

produto2 = {
    'codigo': 2,
    'descrição': 'Café três corações',
    'Quantidade': 67,
    'Valor': 8.00
}

###Adicionando os produtos em uma lista
lista_produtos = []
lista_produtos.append(produto1)
lista_produtos.append(produto2)
##print(lista_produtos)
###Como acessar partes expecificas da lista:
#print(lista_produtos[1]['descrição'])


###Como trazer só os valores
#for item in produto1.values():

###COMO TRAZER TUDO!
#for item in produto1.items():
    #print(item)

###Trazendo uma chave especifica:
print(produto2.get('Valor'))