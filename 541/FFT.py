from numpy.fft import fft, ifft
from numpy import real, imag

def polynomial_multiply(a_coeff_list, b_coeff_list):
    # Return the coefficient list of the multiplication 
    # of the two polynomials 
    # Returned list must be a list of floating point numbers.
    # Please convert list from complex to reals by using the 
    # real function in numpy.
    # your code here
    n = len(a_coeff_list)
    m = len(b_coeff_list)
    
    total_size = n + m - 1
    
    a_coeff_padded = a_coeff_list + [0] * (total_size - n)
    b_coeff_padded = b_coeff_list + [0] * (total_size - m)
    
    fft_a = fft(a_coeff_padded)
    fft_b = fft(b_coeff_padded)
    
    fft_c = fft_a * fft_b
    
    c_coeff_padded = ifft(fft_c)
    
    c_real = [real(x) for x in c_coeff_padded]
    
    return c_real