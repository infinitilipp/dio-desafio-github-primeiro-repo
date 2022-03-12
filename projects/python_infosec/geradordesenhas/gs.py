import random, string 


##definir o tamanho, boa pratica em info sec = 16 p mais
##tamanho = 16
tamanho = int(input('Digite o tamanho de senha que você deseja:'))

##letras em geral, 0 a 9
##se for ascii_lowercase, só letras minusculas
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.:;/?'

rnd = random.SystemRandom() ##os.urandom -> gera numeros aleatorios a partir de fontes fornecidas pelo SO

##lista c caracteres randomicos para cada i no range tamanho (gerará nova letra, simbolo aleatorio -> ate 16 caracteres
print(''.join(rnd.choice(chars) for i in range(tamanho)))
