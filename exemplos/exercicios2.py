#Passo 1. nome do cliente
nome_do_cliente = input('Seja bem vindo! Qual seu nome por favor ?:')

#Passo 2. endereço
endereco = input('endereço de entrega')

#Passo 3. receber o pedido
pedido = input('Digite qual e o sabor da sua pizza:\n (Mussarela| Clabreza |Portuguesa) :')

print(f'Sr.{nome_do_cliente} seu pedido sera entregue no {endereco}, o sabor da escolido é {pedido}')

#Passo4. opçoes (elfi traducao em pt-br senao entao)
if pedido == 'Mussarela':
    print(f'Sr(a){nome_do_cliente}, o seu pedido sera enteregure no {endereco}, sabor escolido é: {pedido}')
elif pedido == 'Calabreza':
    print('Muito obrigado')
elif pedido 'Portuguesa':