import numpy as np

def polynomial_multiply(a_coeffs, b_coeffs):
    n = len(a_coeffs)
    size = 1
    
    while size < len(a_coeffs) + len(b_coeffs):
        size *= 2
        
    a_fft = np.fft.fft(a_coeffs, size)
    b_fft = np.fft.fft(b_coeffs, size)
    c_fft = a_fft * b_fft
    
    c_coeffs = np.fft.ifft(c_fft).real
    
    return np.round(c_coeffs).astype(int)

def check_sum_exists(a, b, c, n):
    
    a_coeffs = [0] * (n + 1)
    b_coeffs = [0] * (n + 1)

    for num in a:
        a_coeffs[num] = 1
    for num in b:
        b_coeffs[num] = 1

    c_coeffs = polynomial_multiply(a_coeffs, b_coeffs)
    
    for num in c:
        if num <= n and c_coeffs[num] > 0:
            return True
    
    return False