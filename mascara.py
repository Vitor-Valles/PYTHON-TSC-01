'''
FORMATAÇÃO DE MÁSCARA

Assim como em outras linguagens, é possivel utilizar identificadores para representar os tipos de dados armazenados nas variáveis que devem ser exibidas na tela.
O Python utiliza a formatação comum entre várias linguagens de desenvolvimento para as máscaras.

Exemplo na tabela avaixo de Máscara, Tipo de Dados e Descrição:

%d ou %i        Int (inteiro)   Exibe um valor inteiro.

%f              Float ou double     Exibe um valor decimal.

%id             Long Int            Exibe um número inteiro longo.

%e ou %E        Float e double      Exibe um número exponecial (número científico).

%c              Char (caractere)    Exibe um caractere.

%x ou %X        Int                 Exibe um número inteiro no formato hexadecimal.

%s              Char                Exibe uma cadeia de caracteres (string).

%r              Boolean             Exibe True ou False (verdeiro ou falso).

Vide exemplos abaixo de aplicação:
'''

fruta = 'Laranja'
print(fruta)
print('Meu suco favorito é de '+ fruta)#Usar , por padrão
print('Meu suco favorito é de...',fruta)
print('Suco de %s é o meu favorito' %fruta)

#Exercícío: exiba a mensagem "Suco de laranja é meu favorito, amo Laranja."

print('Suco de %s e meu favorito,'%fruta, 'amo %s '%fruta)
print('Suco de %s e meu favorito, amo %s.'% (fruta,fruta))
print('Suco de {0} e meu favorito, amo {0}.' .format(fruta))

#Fim do exercício

print('Suco de {0} e meu favorito!'.format(fruta))

cor1 = 'azul'
cor2 = 'Vermelha'
cor3 = 'Preta'

print('Gosto do céu {}, a flor {} e pra o carro prefero a cor {}'.format(cor1,cor2,cor3))
print('Gosto do céu {0}, a flor {1} e pra o carro prefero a cor {0}'.format(cor1,cor2))

conta = 10/3
print(conta)

print('O valor da conta é %f' %conta)
print('O valor da conta é %i' %conta)
print('O valor da conta é {}'.format(conta))
print('O valor da conta é %.2f' %conta)
print('O valor da conta é {:.2f}'.format(conta))

