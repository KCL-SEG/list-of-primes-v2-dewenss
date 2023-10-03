"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if number_of_primes > 0:
        while len(list) < number_of_primes:
            is_prime = True
            for j in range(2,count):
                if count%j == 0:
                    is_prime = False
                    break 
            if is_prime:
                list.append(count)
            count+=1
        return list
    else:
        raise ValueError(f"{number_of_primes} should be greater than 0")

ten_primes = primes(10)

print(ten_primes)