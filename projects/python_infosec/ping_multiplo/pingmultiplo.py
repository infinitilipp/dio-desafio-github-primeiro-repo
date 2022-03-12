##esse py fará ping em diversos hosts ou IPs q percorre num arquivo de texto
import os
import time

with open('hosts.txt') as file: ##com a abertura de hosts.txt como arquivo:
	dump = file.read() ##essa var lerá o arquivo
	dump = dump.splitlines() ##vai colocar os IPs certo em cada linha separada
##, ao inves de espalhado na vertical
	
	for ip in dump:
		print('Verificando o ip:', ip)
		print('-'*60)
		os.system('ping -w 2 {}'.format(ip))
		print('-'*60)
		time.sleep(5)
