def fibonacci(numero: int) -> int:
    num1 = 0
    num2 = 1
    
    while numero > num1 and numero > num2:
        temp = num1 + num2
        num1 = num2
        num2 = temp
        
        if numero == num1 or numero == num2:
            return True
        
    return False
   

if __name__ == '__main__':
    numero = int(input("Digite aqui o número: "))
    if fibonacci(numero):
        print(f"O número {numero} pertence a sequência de Fibonacci!")
    else:
        print(f"O número {numero} não pertence a sequência de Fibonacci!")