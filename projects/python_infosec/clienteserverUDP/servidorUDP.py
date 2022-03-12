import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host, port)) ##faz a ligação entre cliente e servidor pelo: host e porta
mensagem = '\nServidor: Salut, cliente'

while 1: ##enqnt for true, se a ligação der certo -> vai receber 4096bytes atravez do objeto de conexao, vai guardar dentro de dados
	dados, end = s.recvfrom(4096)
	
	if dados: ##se houver dados entre essa ligação, se a ligaçao for true, recebe resposta (troca de msg e resposta)
		print('Servidor enviando mensagem...')
		##enviar a nossa msg via pacotes UDP pra la
		s.sendto(dados + (mensagem.encode()), end)
