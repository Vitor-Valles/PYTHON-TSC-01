idade = int(input('Informe sua idade:'))


#Em Python a sintaxe de condicional e diferente, em vez de if(Condição){Verdadeiro}else{Falso} ele passa a ser if Condição: Verdadeiro else: Falso
if idade >=21:
    print('Você é adulto')
elif idade >=18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')