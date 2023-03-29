# Esta función retorna `True` si el número es impar
def is_odd2(num):
    return (num % 2) != 0

# your function here
is_odd = lambda num: num % 2 != 0

print(is_odd(5))
print(is_odd(2))



print(is_odd2(5))
print(is_odd(10))
