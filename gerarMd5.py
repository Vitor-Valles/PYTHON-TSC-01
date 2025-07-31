import hashlib #Biblioteca para calular funções de hash md5, sha-1, sha-256 e outros

arquivo = input('Digite o nome do arquivo: ')

#Tratamento de erro para evitar que o programa quebre caso o arquivo não existir. Bloco e codigo e axceção
try:
#With garante que o arquivo em modo binario seja fechado corretamente após o uso
    with open(arquivo, 'rb') as f:
#Cria um objeto hash usando o algoritimo md5
        md5 = hashlib.md5()
#Lê  o arquivo em blocos de 4096 byts para arquivos grandes, evitando o consumo excessivo de memória
        for chunk in iter(lambda: f.read(4096), b""):
#Adciona o conteúdo do bloco ao hash
            md5.update(chunk)
#Exibe o hash md5 em formato hexadecimal
            print(f"MD5: {md5.hexdigest()}")
#Fechamento do bloco try
except FileExistsError:
    print('Arquivo não encontrado.')