import time  # We need this to measure how long our code takes to run


class BinaryNumber:
    """ This class helps us work with binary numbers - like converting 
    between regular numbers (decimal) and binary (0s and 1s) """

    def __init__(self, n):
        # Store the regular number (like 42)
        self.decimal_val = n
        # Convert it to binary (like '101010') and make it a list
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        # This just makes our number print nicely when we look at it
        return ('decimal=%d binary=%s' %
                (self.decimal_val, ''.join(self.binary_vec)))


def binary2int(binary_vec):
    # Converts a list of binary digits back to a BinaryNumber
    # Like ['1','0','1'] -> BinaryNumber(5)
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
    # Splits a binary number into two halves
    # Like '1010' -> '10' and '10'
    # Super useful for our divide-and-conquer approach!
    return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
    # This is like multiplying by 2^n by adding zeros to the end
    # Similar to how adding a zero in decimal multiplies by 10
    return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
    # Makes sure our binary numbers are the same length by adding leading zeros
    # Like padding '10' to '0010' if we're comparing with '1110'
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # Make sure length is even (needed for our algorithm)
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


def quadratic_multiply(x, y):
    # The main function that users will call
    # Converts our fancy BinaryNumber result back to a regular number
    return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):
    # Here's where the actual multiplication magic happens!

    # If numbers are tiny, just multiply them directly
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    # Make sure our numbers are properly formatted
    xvec, yvec = pad(x.binary_vec, y.binary_vec)

    # Split each number into two parts (divide)
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    # Get length for our bit shifts
    n = len(xvec)

    # Now apply the multiplication formula (conquer)
    # It's like FOIL method but with binary numbers!
    term1 = bit_shift(_quadratic_multiply(x_left, y_left), n)
    term2 = bit_shift(_quadratic_multiply(x_left, y_right), n // 2)
    term3 = bit_shift(_quadratic_multiply(x_right, y_left), n // 2)
    term4 = _quadratic_multiply(x_right, y_right)

    # Add all parts together for final result
    return BinaryNumber(term1.decimal_val + term2.decimal_val +
                        term3.decimal_val + term4.decimal_val)


def time_quadratic_multiply(x, y, f):
    # Measures how long our multiplication takes
    # Like using a stopwatch in a science experiment
    start = time.time()
    result = f(x, y)
    return (time.time() - start) * 1000  # Convert to milliseconds
