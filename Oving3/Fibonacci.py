
number = int(input("Hvor stor fibonaccirekke vil du skrive ut?: "))

def fibonacci(k):
    n1 = 0
    n2 = 1

    fibList = [0,1]

    for i in range(0 , k-1):
        fibonacciNumber = n1 + n2
        n1 = n2
        n2 = fibonacciNumber
        fibList.append(fibonacciNumber)
    return fibList

result = str(sum(fibonacci(number)))


print(str(fibonacci(number)))
print("summen av listen er " + result)
 
fibonacci(number)

