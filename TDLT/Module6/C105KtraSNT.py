def check_primes(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
print(check_primes(16))