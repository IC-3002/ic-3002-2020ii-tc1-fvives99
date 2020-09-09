import math


def e_cuadratica(n):
    i=0
    result = 0
    while i<=n:
    	result += 1/math.factorial(i)
    	i+=1
    return result


def e_lineal(n):
	result = 0
	factorial = 1
	for i in range(1,n):
		result += 1/factorial
		factorial *= i
	return result


