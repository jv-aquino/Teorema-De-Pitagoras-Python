#Aplicação do Teorema de Pitágoras(a² = b² + c²) com 1 valor desconhecido em Python - v1.1.0 João Vitor de Aquino, 26/06/2020
#Disponível em: https://github.com/jv-aquino/TeoremaDePitagorasPython/
#Declarando as variáveis Hipotenusa(a), Catetos (b, c)
#E outras variáveis referentes aos parâmetros, valores e validações(parametro, paramDesconhecido, valorFinal, valorInvalido, valido)
a, b, c = float, float, float
parametro, paramDesconhecido, valido = str, str, True
valorFinal, valorInvalido = '---------------\nUm erro ocorreu', '\nValor(es) Inválido(s)'

#Descobrindo o parâmetro desconhecido
parametro = input('Qual é o parâmetro desconhecido (a, b ou c)? \n')

#Definindo o valor dos parâmetros conhecidos 

#Obtendo o valor de "b" e "c" caso o parâmetro desconhecido seja "a"
if parametro == 'a' or parametro == 'A':
 b = input('Qual o valor de b? \n')
 c = input('Qual o valor de c? \n')
 #Transformando valores em floats, se possível
 try:
  b,c = float(b), float(c)
 except ValueError:
  print(valorInvalido)
  valido = False
  
#Obtendo o valor de "a" e "c" caso o parâmetro desconhecido seja "b"
elif parametro == 'b' or parametro == 'B':
 a = input('Qual o valor de a? \n')
 c = input('Qual o valor de c? \n')
 #Transformando valores em floats, se possível
 try:
  a,c = float(a), float(c)
 except ValueError:
  print(valorInvalido)
  valido = False

#Obtendo o valor de "a" e "b" caso o parâmetro desconhecido seja "c"
elif parametro == 'c' or parametro == 'C':
 a = input('Qual o valor de a? \n')
 b = input('Qual o valor de b? \n')
 #Transformando valores em floats, se possível
 try:
  a,b = float(a), float(b)
 except ValueError:
  print(valorInvalido)
  valido = False

#Mensagem de erro caso o parâmetro não seja válido
else: 
 print('Esse parâmetro (\"' + parametro + '\") é inválido :/ \nOs parâmetros aceitados são \"a\"(Hipotenusa), \"b\"(Cateto Oposto) e \"c\"(Cateto Adjacente)')

#Com os valores estabelecidos, agora é hora de calcular ;)
#Verficando se os valores estão corretos
if valido == True:
#Calculando o valor da Hipotenusa(a), caso esse seja o valor desconhecido
 if parametro == 'a' or parametro == 'A': 
  a = (b * b) + (c * c)
  a = a**(0.5)
  a = str(a)
  valorFinal = ('O valor da Hipotenusa(a) é ' + a)

#Calculando o valor da Cateto Oposto(b), caso esse seja o valor desconhecido
 elif parametro == 'b' or parametro == 'B':
  b = (a * a) - (c * c)
  b = b**(0.5)
  b = str(b)
  valorFinal = ('O valor do Cateto Oposto(b)  é ' + b)

#Calculando o valor da Cateto Adjacente(c), caso esse seja o valor desconhecido
 elif parametro == 'c' or parametro == 'C':
  c = (a * a) - (b * b)
  c = c**(0.5)
  c = str(c)
  valorFinal = ('O valor do Cateto Adjacente(c) é ' + c)
 else:
  None
else:
 None  
#Printando o valor final do parâmetro desconhecido
print(valorFinal)
