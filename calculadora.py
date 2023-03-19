def adicao(x,y):
    return(x + y)

def subtracao(x,y):
    return(x - y)

def multiplicacao(x,y):
    return(x * y)

def divisao(x,y):
    return(x / y)

print("Qual operação você quer fazer ?")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opc = int(input("Digite sua opção (1/2/3/4):"))

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

if opc == 1:
    print(num1, "+", num2, "=", adicao(num1,num2))
elif opc == 2:
    print(num1, "-", num2, "=", subtracao(num1,num2))
elif opc == 3:
    print(num1, "*", num2, "=", multiplicacao(num1,num2))
elif opc == 4:
    print(num1, "/", num2, "=", divisao(num1,num2))
else:
    print("Operação ou opção invalida !!!")
