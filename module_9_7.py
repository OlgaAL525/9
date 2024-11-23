def is_prime(func):
    def wrapper(*args):
        k = sum_three(*args)
        print(k)
        i = 2
        m = 'Простое'
        while i <= (k//2 + 1):
            if not k % i:
                m = 'Составное'
                break
            else:
                i += 1
        return m
    return wrapper

def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_

result = is_prime(sum_three())
print(result(7,9,1))


