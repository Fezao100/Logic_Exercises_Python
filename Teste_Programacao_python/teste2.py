#Função para encontrar se o número pertence a sequencia de fibonacci
def fibonacci(num):
    n1 = 0
    n2 = 1
    n3 = 0

    if num == n1 or num == n2:
        return print(f"O número {num} pertence a sequência de Fibonacci")
    
    while n3 < num:
        n3 = n1 + n2
        n1 = n2
        n2 = n3    
        
    if n3 == num:
        return print(f"O número {num} pertence a sequência de Fibonacci")
    else:
        return print(f"O número {num} não pertence a sequência de Fibonacci")
        
num_entrada = int(input("Digite um número: "))
fibonacci(num_entrada)