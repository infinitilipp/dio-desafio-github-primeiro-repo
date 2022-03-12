import socket

##obj de conexao
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
porta = 5433 ##porta q vai se conectar no sv
mensagem = 'Bonsoir, servidor'


##tentarei enviar e receber essa msg
try:
	print('Cliente:' + mensagem)
	s.sendto(mensagem.encode(), (host, 5432)) ##empacota a msg e envia ela com pacotes UDP para o servidor
##enviará ela no host na porta 5432, q é a q estará ouvindo

##2 var, dados e servidor
##elas receberão do sv uma resposta de 4096 bytes
	dados, servidor = s.recvfrom(4096) ##o obj connect vai receber do sv (recievefrom) 4096 bytes, a resp esperada
	dados = dados.decode() ##desempacota os dados -> a mensagem
	##vai printar os dados
	print("Cliente: " + dados)
##fechará a conexão pra q n fique em loop
finally:
	print('Cliente: Fechando a Conexão')
	s.close()
