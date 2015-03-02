def is_prime(n):
    prime=True
    for i in range(2,n-1):
        if n%i==0:
            prime=False
    return prime


def prime_pair(numbers):
    prime=False
    for number in numbers:
        for number1 in numbers:
            if is_prime(number+number1)==True:
                prime=True
    return prime

print(prime_pair([3,5,7]))
    
