texto = 'manipulação de textos no Python'
print(texto)

#Análise
print(len(texto))#Mostra o valor atribuido a uma variavel ou valor dentro do print.
print(texto.count('o'))#Conta a contidade de uma letra especifica em um texto.
print(texto.count('o',0,13))#Conta a contidade de uma letra dentro de um espaço de caractéres.
print(texto.find('tos'))#Aonde inicia a posição de inicio.
print('Python' in texto)#Procura a palavra dentro do texto e retorna se e verdadeira ou falso.

#Transformação
print(texto.replace('Python','Cobra'))#Substitui uma palavra por outra no texto, mostrando-nos o resultado no print(PS:Não altera o valor da variavel).
texto = texto.replace('Python','Cobra')#Assim ele substitui o valor dentro da variavel permanentimente (Também se pode fazer texto = texto.replace('Python','Cobra')).
print(texto.lower())#Coloca o texto como maisculo.
print(texto.upper())#Coloca o texto como minusculo.
print(texto.capitalize())#Coloca a primera letra como maiscula.
print(texto.title())#Coloca todos as palavras iniciando como se fosse titulo(Iniciando com letra maiscula).
textoEspaco = '     Texto com espaço        '
print(textoEspaco.strip())#Remove todos os espaços deixando os do meio.
print(textoEspaco.rstrip())#Remove todos os espaços a direita.
print(textoEspaco.lstrip())#Remove todos os espaços a esquerda.
print(textoEspaco.replace(" ",""))#Remove todos os espaços.

#Divisão
print(texto.split())#Divide o textos em partes.
print('-'.join(texto))#Uni as letra com ifen.

#Fatiamento
print(texto[5])#Retorna o caractere da posição 5 pois ele conta a partir do 0.
print(texto[7:19])#Mostra o intervalo entre 7 e 19
print(texto[7:19:2])#Mostra o intervalo entre 7 e 19, e pula de 2 em 2
print(texto[:7])#Ele mostra do 0 ao 7
print(texto[7:])#Ele mostra do 7 ate o final
print(texto[7::3])#Ele mostra em 3 em 3 a partir do 7