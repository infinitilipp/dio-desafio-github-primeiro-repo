import socket ##essa biblioteca chama a api socket q relaciona a placa de rede e SO,
##abertura e fechamento de conexao
import sys ##essa biblioteca fornece acesso a algumas var e funçoes
##relacionadas ao interpretador

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	except socket.error as e: ##caso de a exceção
		print("A conexão falhou!")
		print("Erro: {}".format(e))
		sys.exit() ##fecha o programa
	
	print("Socket criado com sucesso")
	
	HostAlvo = input("Digite o host ou IP a ser conectado: ")
	PortaAlvo = input("Digite a porta a ser conectada: ")
	
	try:
		s.connect((HostAlvo, int(PortaAlvo))) ##pede o address dentro, e portaalvo precisa ser int
		
		print("Cliente TCP conectado com sucesso no host " + HostAlvo + " e na porta " + PortaAlvo)
		s.shutdown(2) ##mostra q foi conectado com sucesso e ja fecha a conexao p n ficar em loop 
	except socket.error as e:
		print("Não foi possível conectar no host " + HostAlvo + " e na porta " + PortaAlvo)
		print("Erro: {}".format(e))
		sys.exit()
		
if __name__ == "__main__":
	main()
