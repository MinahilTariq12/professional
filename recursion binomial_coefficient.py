# i check the formula of binomial coefficient through internet
def return_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return return_binomial_coefficient(n - 1, k - 1) + return_binomial_coefficient(n - 1, k)
print(return_binomial_coefficient(9, 2))

