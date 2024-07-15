def polynomial_formatter(func):
    def wrapper(*args):
        result = func(*args)
        print_polynomial(result)
        return result
    return wrapper

def print_polynomial(coefficients):
    for i, coefficient in enumerate(coefficients):
        if coefficient != 0:
            if i == 0:
                print(coefficient, end='')
            elif i == 1:
                print(coefficient, end='x')
            else:
                print(f'{coefficient}x^{i}', end='')
            if i != len(coefficients) - 1:
                print(' + ', end='')
    print()

@polynomial_formatter
def polynomial_multiplication(poly1, poly2):
    m, n = len(poly1), len(poly2)
    result = [0] * (m + n - 1) 

    for i in range(m):
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j]
    return result

# Example usage
poly1 = [1, -5, 3]
poly2 = [1, 2] 
product = polynomial_multiplication(poly1, poly2)