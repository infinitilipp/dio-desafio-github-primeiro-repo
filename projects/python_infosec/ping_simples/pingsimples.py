import os ##importa o modulo/biblioteca os (integra os programas e recursos 
##do sistema operacional
 
print("#" * 60) ##imprime # 60x


##cria var q recebe do usuario um ip
ip_ou_host = input("Digite o IP ou host a ser verificado: ")


print("-" * 60) ##imprime - 60x

##esse metodo da biblio os trará todos os comandos intimamente ligados ao sistema
##como o ping
os.system('ping -w 4 {}'.format(ip_ou_host))
print("-" * 60)
