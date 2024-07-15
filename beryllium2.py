from functools import wraps
def poly_formatter(func):
    @wraps(func)
    def formatter_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)       
        #Convert the result list into polynomial format
        polynomial_str = ""
        for i, coeff in enumerate(result):
            if coeff != 0:
                term = 'x^{}'.format(i) if i > 0 else ''
                polynomial_str += (' + ' if coeff > 0 and polynomial_str else ' ') + f'{coeff}{term}'
        polynomial_str = polynomial_str.lstrip(' + ')
        print(f'The polynomial result is:  {polynomial_str}')
        return result
    return formatter_wrapper

@poly_formatter
def polynomial_multiplication(poly1, poly2):
    m, n = len(poly1), len(poly2)
    result = [0] * (m + n - 1)
    for i in range(m): 
        for j in range(n): 
            result[i + j] += poly1[i] * poly2[j] 
    return result
    
poly1 = [1, -5, 3] 
poly2 = [1, 2]    
product = polynomial_multiplication(poly1, poly2)
print(product)