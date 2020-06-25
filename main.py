#Aplicação do Teorema de Pitágoras(a² = b² + c²) com 1 valor desconhecido em Python - v1.0.0 João Vitor de Aquino, 24/06/2020
# Disponível em: https://github.com/jv-aquino/TeoremaPitagorasPy
#Declarando as variáveis Hipotenusa(a), Catetos (b,c) e outras variáveis referentes aos parâmetros (parametro, paramDesconhecido, paramConhecido1, paramConhecido2)
a = float
b = float 
c = float 
parametro = str
paramDesconhecido = str
paramConhecido1 = str
paramConhecido2 = str

#Descobrindo o tipo do parâmetro desconhecido
parametro = input('Qual é o parâmetro desconhecido (a, b ou c)? \n')

#Definindo o valor dos parâmetros conhecidos

#Obtendo o valor de "b" e "c" caso o parâmetro desconhecido seja "a"
if parametro == 'a' or parametro == 'A':
 paramConhecido1 = 'Qual o valor de b? \n'
 paramConhecido2 = 'Qual o valor de c? \n'
 paramDesconhecido = 'a'
 b = float(input(paramConhecido1))
 c = float(input(paramConhecido2))

#Obtendo o valor de "a" e "c" caso o parâmetro desconhecido seja "b"
elif parametro == 'b' or parametro == 'B':
 paramConhecido1 = 'Qual o valor de a? \n'
 paramConhecido2 = 'Qual o valor de c? \n'
 paramDesconhecido = 'b'
 a = float(input(paramConhecido1))
 c = float(input(paramConhecido2))

#Obtendo o valor de "a" e "b" caso o parâmetro desconhecido seja "c"
elif parametro == 'c' or parametro == 'C':
 paramConhecido1 = 'Qual o valor de a? \n'
 paramConhecido2 = 'Qual o valor de b? \n'
 paramDesconhecido = 'c'
 a = float(input(paramConhecido1))
 b = float(input(paramConhecido2))
 
#Mensagem de erro caso o parâmetro não seja válido
else: 
 print('Esse parâmetro é inválido :/ os parâmetros aceitados são \"a\"(Hipotenusa), \"b\"(Cateto Oposto) e \"c\"(Cateto Adjacente)')

#Com os valores estabelecidos, agora é hora de calcular ;)

#Calculando o valor da Hipotenusa(a), caso esse seja o valor desconhecido
if paramDesconhecido == 'a':
 a = (b * b) + (c * c)
 a = a**(0.5)
 a = str(a)
 print('O valor da Hipotenusa(a) é ' + a)

#Calculando o valor da Cateto Oposto(b), caso esse seja o valor desconhecido
elif paramDesconhecido = 'b':
 b = (a * a) - (c * c)
 b = b**(0.5)
 b = str(b)
 print('O valor do Cateto Oposto(b)  é ' + b)

#Calculando o valor da Cateto Adjacente(c), caso esse seja o valor desconhecido
elif paramDesconhecido = 'c':
 c = (a * a) - (b * b)
 c = c**(0.5)
 c = str(c)
 print('O valor do Cateto Adjacente(c) é ' + c)

#Mais uma mensagem de erro caso o parâmetro seja inválido
else:
 print('O pârametro é inválido :( ')
