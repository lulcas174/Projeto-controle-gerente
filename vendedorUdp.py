import socket
import socket as skt

ip_Servidor = '127.0.0.1'
porta_Servidor = 9000

udp = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

destino = (ip_Servidor, porta_Servidor)
dados_vendedor = {}
codigo_operacao = input('Informe seu codigo de vendedor:\n') #codigo de vendedor: V3nD321
udp.sendto(codigo_operacao.encode("utf8"), destino)
while codigo_operacao != 'V3nD321':
    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    codigo_operacao = input('Informe um codigo de vendedor válido:\n')
    udp.sendto(codigo_operacao.encode("utf8"), destino)

msg, servidor = udp.recvfrom(1024)
print('=================================')
print(msg.decode())
print('=================================')

while True:
    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    nome_vendedor = input()

    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    id_loja = input()

    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    data_venda = input()

    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    valor_vendido = input()

    dados_vendedor.update({'nome_vendedor':nome_vendedor, 'id_loja':id_loja,
                           'data_venda': data_venda, 'valor_vendido': valor_vendido})
    msg = str(dados_vendedor)
    udp.sendto(msg.encode("utf8"), destino)

    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())

    msg, servidor = udp.recvfrom(1024)
    print(msg.decode())
    msg = input()
    udp.sendto(msg.encode("utf8"), destino)
    if msg.lower() == 'n' or msg.lower() == 'não':
        socket.SHUT_RDWR
        break
# udp.close()