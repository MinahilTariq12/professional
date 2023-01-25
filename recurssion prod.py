def recurssion_product(n):
    if n <= 1:
        return n
    return n * recurssion_product(n - 1)
n = 16
print(recurssion_product(n))

