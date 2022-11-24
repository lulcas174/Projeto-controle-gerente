import socket as skt

ip_Servidor = '127.0.0.1'
porta_Servidor = 9000

udp = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
destino = (ip_Servidor, porta_Servidor)
dados_vendedor = {}
codigo_operacao = input('Informe seu codigo de Gerente:\n') #codigo de gerente: G3R123
udp.sendto(codigo_operacao.encode("utf8"), destino)
while codigo_operacao != 'G3R123':
    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    codigo_operacao = input('Informe um codigo de gerente válido:\n')
    udp.sendto(codigo_operacao.encode("utf8"), destino)

msg, servidor = udp.recvfrom(1024)
print('=================================')
print(msg.decode())
print('=================================')

while True:
    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    opcao = input()
    if opcao == '6':
        udp.sendto(opcao.encode("utf8"), destino)
        break
    elif opcao == '4' or opcao == '5':
        udp.sendto(opcao.encode("utf8"), destino)
        msg, servidor = udp.recvfrom(1024)
        print(msg.decode())
    elif opcao != '4' or opcao != '5':
        udp.sendto(opcao.encode("utf8"), destino)
        msg, servidor = udp.recvfrom(1024)
        print(msg.decode())
        dados = input()
        udp.sendto(dados.encode("utf8"), destino)
        msg, servidor = udp.recvfrom(1024)
        print(msg.decode())
# udp.close()