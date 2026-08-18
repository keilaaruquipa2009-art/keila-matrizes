vendas = [
    [1200,1500,1100],
    [1000,1300,1400],
    [900,1700,1600]
]
#Dados complementares
nomes_vendedores = ['Luiz','Carlos','Dias']
nomes_meses = ['Janeiro','Fevereiro','Março']
#Etapa 1: Exibição Organizada
print(nomes_meses)
for i in range(len(vendas)):
    Linha = vendas [i]
    print('' *12)
    print(" ".join(f'{m:>6}' for m in nomes_meses))
    nomes = ['Luiz','Carlos','Dias']
    nomes2 = nomes
    nomes[0] = 'Lucas'
    print(nomes)
    print(nomes2)
    nomes3 = nomes[:]
    nomes3[0]='Luiz'
    print(nomes)
    print(nomes3)
    print(nomes2)
    print(f'{nomes[0]:>10}')
    print(f'{nomes[0]:<10}#')