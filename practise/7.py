def factorial(number):
    answer = 1
    for i in range(number,1,-1):        
        answer *= i
    return answer
print(factorial(-5))