import socket

ip = ''
porta = 9000
consulta = []
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (ip, porta)
udp.bind(servidor)
while True:
    print('Aguardando Conexão...')
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode()
    if msg == 'G3R123':
        print('Um Gerente Conectado Com Sucesso.')
        conectado = ('Gerente Conectado Com Sucesso.')
        udp.sendto(conectado.encode("utf8"), cliente)
        while True: 
            msg = """O Que Deseja Consultar?\n
            1-Total De Vendas De um Vendedor\n
            2-Total De Vendas De uma Loja\n
            3-Total De Vendas da Rede de Lojas Durante um Periodo\n
            4-Melhor Vendedor\n
            5-Melhor Loja\n
            6-Sair"""
            
            udp.sendto(msg.encode("utf8"), cliente)
            msg, cliente = udp.recvfrom(1024)
            msg = msg.decode()
            if msg == '6' or msg.lower() == 'sair':
                break
            if msg == '1' or msg.lower() == 'total de vendas de um vendedor':
                nome = 'informe o nome do vendedor'
                udp.sendto(nome.encode("utf8"), cliente)
                nome_vendedor, cliente = udp.recvfrom(1024)
                nome_vendedor = nome_vendedor.decode()
                count = 0
                for i, v in enumerate(consulta):
                    if consulta[i]['nome_vendedor'] == nome_vendedor:
                        count += 1
                vendedor = (f"O vendedor {nome_vendedor} fez {count} vendas")
                udp.sendto(vendedor.encode("utf8"), cliente)

            elif msg == '2' or msg.lower() == 'total de vendas de uma loja':
                loja = 'informe o id da loja'
                udp.sendto(loja.encode("utf8"), cliente)
                id_loja, cliente = udp.recvfrom(1024)
                id_loja = id_loja.decode()
                count = 0
                for i, v in enumerate(consulta):
                    if consulta[i]['id_loja'] == id_loja:
                        count += 1
                loja = (f"O total de Vendas da Loja foi De {count}")
                udp.sendto(loja.encode("utf8"), cliente)
            elif msg == '3' or msg.lower() == 'total de vendas da rede de lojas durante um periodo':
                data = 'informe uma data'
                udp.sendto(data.encode("utf8"), cliente)
                data_venda, cliente = udp.recvfrom(1024)
                data_venda = data_venda.decode()
                count = 0
                if '/' in data_venda:
                    data_venda = data_venda.replace("/", "")
                elif '-' in data_venda:
                    data_venda = data_venda.replace("-", "")
                for i, v in enumerate(consulta):
                    if consulta[i]['data_venda'] == data_venda:
                        count += 1
                totalLoja = (
                    f"O total de vendas da loja durante o período especificado foi de {count} vendas")
                udp.sendto(totalLoja.encode("utf8"), cliente)
            elif msg == '4' or msg.lower() == 'melhor vendedor':
                melhorVend = 0
                melhorVend1 = 0
                vend = ''
                vend1 = ''
                for i, v in enumerate(consulta):
                    if consulta[i]['valor_vendido'] > melhorVend:
                        melhorVend = consulta[i]['valor_vendido']
                        vend = consulta[i]['nome_vendedor']
                if len(consulta) > 1:
                    for i, v in enumerate(consulta):
                        j = i + 1
                        aux = 0
                        for j, va in enumerate(consulta):
                            if consulta[i]['nome_vendedor'] == consulta[j]['nome_vendedor']:
                                aux = consulta[i]['valor_vendido'] + \
                                    consulta[j]['valor_vendido']
                        if aux > melhorVend1:
                            melhorVend1 = aux
                            vend1 = consulta[i]['nome_vendedor']
                if (melhorVend > melhorVend1):
                    melhorVendedor = (
                        f"O vendedor {vend} foi o melhor com R$ {melhorVend} em vendas")
                    udp.sendto(melhorVendedor.encode("utf8"), cliente)
                else:
                    melhorVendedor = (
                        f"O vendedor {vend1} foi o melhor com R$ {melhorVend1} em vendas ")
                    udp.sendto(melhorVendedor.encode("utf8"), cliente)
            elif msg == '5' or msg.lower() == 'Melhor Loja':
                vendLoja = 0
                vendLoja1 = 0
                loja = ''
                loja1 = ''
                for i, v in enumerate(consulta):
                    if consulta[i]['valor_vendido'] > vendLoja:
                        vendLoja = consulta[i]['valor_vendido']
                        loja = consulta[i]['id_loja']
                for i, v in enumerate(consulta):
                    j = i + 1
                    aux = 0
                    if len(consulta) > 1:
                        for j, v in enumerate(consulta):
                            if consulta[i]['id_loja'] == consulta[j]['id_loja']:
                                aux = consulta[i]['valor_vendido'] + \
                                    consulta[j]['valor_vendido']
                        if aux > vendLoja1:
                            vendLoja1 = aux
                            loja1 = consulta[i]['id_loja']
                if vendLoja > vendLoja1:
                    melhorLoja = (
                        f"A loja {loja} foi a melhor com R$ {vendLoja} vendas em vendas")
                    udp.sendto(melhorLoja.encode("utf8"), cliente)
                else:
                    melhorLoja = (
                        f"A loja {loja1} foi a melhor com R$ {vendLoja1} em vendas")
                    udp.sendto(melhorLoja.encode("utf8"), cliente)
    elif msg == 'V3nD321':
        print("Um vendedor foi conectado")
        conectado = ('Vendedor Conectado Com Sucesso.')
        udp.sendto(conectado.encode("utf8"), cliente)
        while True:
            nome_vendedor = 'Informe seu nome '
            udp.sendto(nome_vendedor.encode("utf8"), cliente)
            id_loja = 'Informe a identificação da loja '
            udp.sendto(id_loja.encode("utf8"), cliente)
            data_venda = 'Informe a data da venda '
            udp.sendto(data_venda.encode("utf8"), cliente)
            valor_vendido = 'Informe o valor vendido '
            udp.sendto(valor_vendido.encode("utf8"), cliente)

            msg, cliente = udp.recvfrom(1024)
            msg = msg.decode()
            dados_vendedor = eval(msg)
            dados_vendedor['valor_vendido'] = float(dados_vendedor['valor_vendido'])
            if '/' in dados_vendedor['data_venda']:
                dados_vendedor['data_venda'] = dados_vendedor['data_venda'].replace(
                    "/", "")
            elif '-' in dados_vendedor['data_venda']:
                dados_vendedor['data_venda'] = dados_vendedor['data_venda'].replace(
                    "-", "")
            consulta.append(dados_vendedor)
            if len(consulta) > 0:
                sucesso = 'OK, dado salvo com sucesso!'
                print(consulta)
                udp.sendto(sucesso.encode("utf8"), cliente)
            else:
                erro = 'ERRO!!Dados inconsistentes, tente novamente!'
                udp.sendto(erro.encode("utf8"), cliente)
            msg = 'Deseja Cadastrar Outra Venda?\n S-Sim\n N-Não'
            udp.sendto(msg.encode("utf8"), cliente)
            msg, servidor = udp.recvfrom(1024)
            msg = msg.decode()
            if msg.lower() == 'n' or msg.lower() == 'não':
                break
    else:
        erro = 'Erro!! Codigo Inválido'
        udp.sendto(erro.encode("utf8"), cliente)