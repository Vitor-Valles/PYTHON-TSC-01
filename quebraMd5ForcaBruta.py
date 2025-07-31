import hashlib #Gerar o hash da senha testada e comparar com o alvo
import itertools #Gerar todas as combinações possiveis de caracteres
import string #Fornecer listas prontas de letras e numeros para o charset
import time #Medir o tempo total de execução da quebra 

#Entrada hash do md5
hash_alvo = input("Digite o hash md5 a ser quebrado: ").strip()

#Definir o conjunto de caracteres a testar a-z 0-9
caracteres = string.ascii_lowercase = string.digits

#Define o tamanho máximo de senha a testar
tamanho_maximo = 4

#f na frente da string é um recurso chamdo f-string para interpolação de variáveis dentro de strings
print(f"Inicinado força bruta para o hash: {hash_alvo}")
print(f"Charset: {caracteres} | Tamanho máximo: {tamanho_maximo}")

inicio = time.time()
encontrado = False

#Loop sobre tamanhos de 1 até o  máximo definido
for tamanho in range(1, tamanho_maximo + 1):
    print(f"Tentanto combinação com {tamanho} caracteres.")
#Gera todas as combinações possiveis como charset e o tamanho atual
    for tentativa in itertools.product(caracteres, repeat=tamanho):
        palavra = ''.join(tentativa)
        hash_teste = hashlib.md5(palavra.encode()).hexdigest()
#Se o hash da tentativa for ingual ao hash alvo, senha foi descoberta
        if hash_teste == hash_alvo:
            print(f"Senha encontrada: {palavra}")
            encontrado = True
            break

        if encontrado:
            break

    if not encontrado:
        print("Senha não encontrada. Tente aumentar o tamanho máximo ou o charset.")

        fim = time.time()
        print(f"Tempo total de execução {fim - inicio:.2f} segundos")


