#Crie um programa em Python para verificar se um número é positivo, negativo ou zero. O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.

#Se o número for maior que zero, exiba a mensagem "O número é positivo." Se for menor que zero, exiba "O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."

#Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara.


#inicio  do programa

#Variavel  para armazenar o valor digitado pelo usuario

numero = int (input("Digite um número: "))

#Estrutura de condiçao que verifica se o numero e positivo,zero  ou negativo

if numero > 0:
    print(f"O número:{numero} é positivo") # se o numero for maior que zero ele sera positivo

elif  numero == 0: #  se o numero for igual a zero ele sera zero
    print(f"O número:{numero} é zero")

else:  # se o numero for menor que zero ele sera negativo
    print(f"O número:{numero} é negativo")
