#Você foi contratado pracriar um progama pra uma autoescola, que deve verificar se a pessoa é maior ou tem 18 anos 

#1.Receber o nome da pesssoa
nome = input('Digite o seu nome:')
#2. Receber a idade da pessoa
idade = int(input('Digite sua idade:'))
#3. possui cnh?
possui_cnh = input('Você possui carteira de habilitacão ? \n (1-Sia / 2-Não):')

#4. verificar se a pessoa  >=18
if idade >= 18:
    if possui_cnh == '1':
     print('Maior de 18 anos e pode dirigir!')
    else:
        print('não pode dirigir, não posui cnh')
else:
    print('menor de idade')